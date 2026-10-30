#!/usr/bin/env python3
"""Run the gangmu identification benchmark against real trees.

Each case pins a real tree (a git URL and a tag or commit) and the component
and version a correct tool must report. The tree is copied under a neutral
name, optionally stripped of its version files, scanned with the installed
gangmu and rule base, and the finding in that directory is graded:

  exact    the reported version is the truth
  range    the reported version is a range that contains the truth
  wrong    another component, or a version that excludes the truth
  missing  nothing reported in that directory
  skipped  the case expects a rule that is not installed (for example a rule from
           a rule pack you did not load); not graded, not a failure

Usage:
  python bench.py                        # every case in cases/
  python bench.py --case lwip-2.2.0      # one case (repeatable)
  python bench.py --rules DIR            # scan with these rules (repeatable)
  python bench.py -o results/latest      # write latest.md and latest.json

A case with a ``binary:`` block is graded the same way but scans a firmware image
instead of a source tree: the pinned tree is cross-compiled (library code only, stripped,
no libc) for the given target with the build recipe of gangmu's
``benchmarks/binary/build_corpus.py``, and the one ELF is scanned. Needs that checkout
(``--gangmu-src``, default ``.gangmu`` or ``../gangmu``) and the target's cross compiler; a case
whose compiler is missing is skipped.

A case with a ``copies:`` list is a vendor SDK: the pinned tree is scanned once,
in place and under its own name (that is how a vendor ships it), and each copy is
graded at its own path against the version the vendor left in its own header.

Clones are cached under ~/.cache/gangmu-bench (or --cache).
"""

from __future__ import annotations

import argparse
import importlib.util
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

HERE = Path(__file__).resolve().parent
NEUTRAL = "vendored_lib"


def load_cases(selected: List[str]) -> List[dict]:
    cases = []
    for path in sorted((HERE / "cases").glob("*.yaml")):
        for case in yaml.safe_load(path.read_text(encoding="utf-8")) or []:
            case["file"] = path.name
            cases.append(case)
    ids = [c["id"] for c in cases]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"duplicate case ids: {sorted(dupes)}")
    if selected:
        unknown = set(selected) - set(ids)
        if unknown:
            raise SystemExit(f"no such case: {sorted(unknown)}")
        cases = [c for c in cases if c["id"] in selected]
    return cases


class FetchError(Exception):
    """A case's source could not be fetched: the case is skipped, the run goes on."""


def fetch(case: dict, cache: Path) -> Path:
    """A checkout of the case's ref, without .git, cached by URL and ref."""
    subdirs = _subdirs(case)
    key = re.sub(r"[^A-Za-z0-9._-]+", "_", f"{case['git']}@{case['ref']}")
    if subdirs:
        key += "+" + hashlib.sha256("\n".join(subdirs).encode()).hexdigest()[:12]
    dest = cache / key
    if (dest / ".complete").exists():
        return dest
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    git = ["git", "-c", "advice.detachedHead=false"]
    subprocess.run(git + ["init", "-q", str(dest)], check=True)
    fetch_cmd = git + ["-C", str(dest), "fetch", "-q", "--depth", "1", case["git"], case["ref"]]
    if subdirs:
        # Only the component's directory of a large repository (an RTOS kernel
        # inside a whole SDK): a blobless fetch and a sparse checkout. A server
        # without partial clone (Gitee) gets the plain shallow fetch.
        subprocess.run(git + ["-C", str(dest), "sparse-checkout", "set", "--no-cone",
                              *[f"/{d}/" for d in subdirs]], check=True)
        attempts = [fetch_cmd[:6] + ["--filter=blob:none"] + fetch_cmd[6:], fetch_cmd]
    else:
        attempts = [fetch_cmd]
    checkout = git + ["-C", str(dest), "checkout", "-q", "FETCH_HEAD"]

    def done(cmd) -> bool:
        # A blobless checkout fetches its blobs then, so the checkout can fail too.
        return (subprocess.run(cmd).returncode == 0
                and subprocess.run(checkout).returncode == 0)

    for attempt in range(3):            # some hosts drop connections now and then
        if any(done(cmd) for cmd in attempts):
            break
        time.sleep(5 * (attempt + 1))
    else:
        shutil.rmtree(dest, ignore_errors=True)
        raise FetchError(f"{case['git']} {case['ref']}: fetch failed three times")
    shutil.rmtree(dest / ".git")
    (dest / ".complete").write_text(case["ref"])
    return dest


def _subdirs(case: dict) -> List[str]:
    sub = case.get("subdir")
    return [] if not sub else [sub] if isinstance(sub, str) else list(sub)


def component_root(case: dict, source: Path) -> Path:
    """The directory a case grades: its first ``subdir`` present, or the checkout."""
    for sub in _subdirs(case):
        if (source / sub).is_dir():
            return source / sub
    if _subdirs(case):
        raise SystemExit(f"{case['id']}: none of {_subdirs(case)} exists at {case['ref']}")
    return source


def prepare(source: Path, work: Path, variant) -> Tuple[str, Path]:
    """pristine; ``{strip: [files]}`` deletes those files (the version must come
    from functions); ``touch`` appends a comment to every C source and header,
    which breaks every byte-for-byte anchor and file-set hash."""
    if variant == "touch":
        name = "touched"
    else:
        name = "pristine" if variant == "pristine" else "stripped"
    root = work / name
    tree = root / NEUTRAL
    shutil.copytree(source, tree, symlinks=True,
                    ignore=shutil.ignore_patterns(".complete"))
    if isinstance(variant, dict):
        for rel in variant.get("strip", []):
            target = tree / rel
            if not target.exists():
                raise SystemExit(f"strip: {rel} does not exist in {source}")
            target.unlink()
    if variant == "touch":
        for path in sorted(tree.rglob("*")):
            if path.suffix in (".c", ".h") and path.is_file() and not path.is_symlink():
                with open(path, "a", encoding="utf-8", errors="replace") as fh:
                    fh.write("\n/* vendor build */\n")
    return name, root


def version_key(text: str) -> Tuple:
    """4.3.4a -> ((4, ''), (3, ''), (4, 'a')); R0.14b -> ((0, ''), (14, 'b'))."""
    key = []
    for part in re.split(r"[.\-_]", text.strip().lstrip("vVrR").lower()):
        match = re.match(r"(\d*)(.*)", part)
        key.append((int(match.group(1)) if match.group(1) else -1, match.group(2)))
    return tuple(key)


def _le(a: str, b: str) -> bool:
    return version_key(a) <= version_key(b)


def grade(findings: List[dict], expect: dict, where: str = NEUTRAL) -> Tuple[str, Optional[dict]]:
    # The component may be found at the copy's root or in a subdirectory of it
    # (TinyCrypt's sources sit in lib/); the shallowest, most confident wins.
    here = [f for f in findings if f.get("directory") == where
            or str(f.get("directory", "")).startswith(where + "/")]
    if not here:
        return "missing", None
    # A package manifest at the root (Arduino library.properties) is a separate, declared
    # finding of the same library; the expected rule's own finding is the one graded.
    own = [f for f in here if f.get("rule_id") == expect["rule"]]
    finding = min(own or here, key=lambda f: (f["directory"].count("/"),
                                              -(f.get("confidence") or 0)))
    if finding.get("rule_id") != expect["rule"]:
        return "wrong", finding
    if expect.get("version") is None:      # the tree states no version to check against
        return "identified", finding
    reported, truth = str(finding.get("version") or ""), str(expect["version"])
    # A vendor that states less than a release number (littlefs's LFS_VERSION is
    # major.minor: 2.11) is matched by any release of it (2.11.3).
    if reported == truth or (reported.startswith(truth + ".") and "~" not in reported):
        return "exact", finding
    if "~" in reported:
        low, high = reported.split("~", 1)
        if _le(low, truth) and _le(truth, high):
            return "range", finding
    return "wrong", finding


def known(verdict: str, reported, expect: dict, variant: str) -> str:
    """``known`` for a wrong answer the case records as understood: the vendor's
    or upstream's own statement is off, and the tool reports what the code is
    (``expect.known``: the reported version, or {variant: reported version},
    with ``known_why``). Shown in the results, not a failure; any other wrong
    answer still is."""
    k = expect.get("known")
    if verdict != "wrong" or k is None:
        return verdict
    want = k.get(variant) if isinstance(k, dict) else k
    return "known" if want is not None and str(want) == str(reported) else verdict


def extras(findings: List[dict], graded: Optional[dict], expect: dict) -> List[dict]:
    """Every finding besides the graded one, labelled. ``unexpected`` is a false
    positive: neither the expected component again, nor a dependency a manifest
    in the tree declares, nor a component the case says this release bundles."""
    out = []
    for f in findings:
        if f is graded:
            continue
        rule = str(f.get("rule_id") or "")
        if rule == expect["rule"]:
            kind = "duplicate"
        elif rule.startswith("declared/"):
            kind = "declared"
        elif rule in expect.get("bundled", []):
            kind = "bundled"
        else:
            kind = "unexpected"
        out.append({"kind": kind, "rule": rule, "directory": f.get("directory"),
                    "version": f.get("version")})
    return out


def find_builder(explicit: Optional[str]):
    """gangmu's build_corpus module, or None when no checkout is at hand."""
    for cand in ([explicit] if explicit else []) + [str(HERE / ".gangmu"), str(HERE.parent / "gangmu")]:
        path = Path(cand) / "benchmarks" / "binary" / "build_corpus.py"
        if path.is_file():
            spec = importlib.util.spec_from_file_location("gangmu_build_corpus", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    return None


def build_image(case: dict, source: Path, work: Path, builder) -> Optional[Path]:
    """A directory holding the stripped firmware image built from *source*, or None."""
    spec = case["binary"]
    recipe = {k: spec[k] for k in ("sources", "exclude", "include", "defines") if k in spec}
    target = spec.get("target", "arm")
    if shutil.which(builder.TARGETS[target]["cc"]) is None:
        return None
    root = work / "image"
    root.mkdir(parents=True)
    elf = work / "build" / "fw.elf"
    elf.parent.mkdir()
    why = builder.build(case["id"], recipe, case["ref"], source, spec.get("opt", "Os"), elf,
                        target=target)
    stripped = elf.with_suffix(".strip.elf")
    if not stripped.exists():
        raise SystemExit(f"{case['id']}: build failed: {why}")
    shutil.copy(stripped, root / "firmware.elf")
    return root


def scan(root: Path, rules: List[str]) -> Tuple[List[dict], float]:
    cmd = ["gangmu", "scan", str(root), "--format", "json", "--no-cache"]
    for r in rules:
        cmd += ["--rules", r]
    start = time.perf_counter()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    elapsed = time.perf_counter() - start
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip()[-2000:])
    return json.loads(proc.stdout)["findings"], elapsed


def run_sdk(case: dict, cache: Path, rules: List[str], installed: set) -> List[dict]:
    """Scan a vendor SDK once and grade every copy it lists at its own path."""
    def row(copy, verdict, finding=None, others=(), seconds=0.0):
        return {
            "case": case["id"], "variant": copy["path"],
            "truth": str(copy["expect"]["version"] or "not stated"),
            "expected_rule": copy["expect"]["rule"],
            "rule": finding and finding.get("rule_id"),
            "reported": finding and finding.get("version"),
            "confidence": finding and finding.get("confidence"),
            "verdict": verdict,
            "directory": finding and finding.get("directory"),
            "other_findings": len(others), "others": list(others),
            "seconds": round(seconds, 2),
        }

    graded = [c for c in case["copies"] if c["expect"]["rule"] in installed]
    out = [row(c, "skipped") for c in case["copies"] if c not in graded]
    for c in out:
        print(f"skipped  {case['id']:22s} {c['variant']}  rule {c['expected_rule']} "
              f"not installed", flush=True)
    if not graded:
        return out
    try:
        source = fetch(case, cache)
    except FetchError as exc:
        print(f"skipped  {case['id']:22s} {exc}", flush=True)
        return out + [row(c, "skipped") for c in graded]
    findings, seconds = scan(source, rules)
    chosen = []
    for copy in graded:
        verdict, finding = grade(findings, copy["expect"], copy["path"].strip("/"))
        verdict = known(verdict, finding and finding.get("version"), copy["expect"], "copy")
        chosen.append((copy, verdict, finding))
    # The SDK's other findings are labelled once, on its first row: against the
    # components the case lists as bundled, or any rule a graded copy expects.
    picked = [f for _, _, f in chosen if f is not None]
    expect = {"rule": None, "bundled": list(case.get("bundled", []))
              + [c["expect"]["rule"] for c in graded]}
    others = extras([f for f in findings if not any(f is p for p in picked)], None, expect)
    for i, (copy, verdict, finding) in enumerate(chosen):
        out.append(row(copy, verdict, finding, others if i == 0 else (), seconds))
        print(f"{verdict:8s} {case['id']:22s} {copy['path']}  reported "
              f"{finding and finding.get('version')} ({finding and finding.get('rule_id')})",
              flush=True)
    for o in others:
        if o["kind"] == "unexpected":
            print(f"         false positive: {o['rule']} {o['version']} at {o['directory']}",
                  flush=True)
    return out


def available_rules(rules: List[str]) -> set:
    """Ids of the rules the scans will load: ``gangmu rules lint`` with the same --rules."""
    cmd = ["gangmu", "rules", "lint"]
    for r in rules:
        cmd += ["--rules", r]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    return {line.split()[1] for line in out.splitlines() if line.startswith("ok ")}


def tool_versions() -> Dict[str, str]:
    out = subprocess.run(["gangmu", "--version"], capture_output=True, text=True).stdout.strip()
    lint = subprocess.run(["gangmu", "rules", "lint"], capture_output=True, text=True).stdout
    roots = [line[5:].rsplit(": ", 1)[0] for line in lint.splitlines() if line.startswith("root ")]
    return {"gangmu": out, "rules": "; ".join(roots), "gangmu_path": which_gangmu() or ""}


def which_gangmu() -> Optional[str]:
    """The ``gangmu`` every scan below runs: the first one on PATH, not necessarily the one
    installed next to the Python that runs this script."""
    found = shutil.which("gangmu")
    return str(Path(found).resolve()) if found else None


def report_tool() -> None:
    """Say which gangmu and which rules are being measured, and warn when that gangmu is not
    the one installed in this Python's environment (a venv's python with another gangmu
    first on PATH measures the wrong tool and says nothing)."""
    path = which_gangmu()
    if path is None:
        print("error: no `gangmu` on PATH; pip install gangmu-sbom", file=sys.stderr)
        raise SystemExit(2)
    meta = tool_versions()
    print(f"gangmu:  {meta['gangmu']}  ({path})")
    print(f"rules:   {meta['rules'] or 'none found'}")
    own = Path(sys.prefix)
    on_path = Path(shutil.which("gangmu") or "")
    if own not in on_path.parents and Path(sys.executable).parent != on_path.parent:
        print(f"warning: this gangmu is not in the Python environment running bench.py "
              f"({own}); put that environment's bin first on PATH to measure its gangmu "
              f"and rules", file=sys.stderr)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--case", action="append", default=[])
    p.add_argument("--rules", action="append", default=[])
    p.add_argument("--cache", default=os.environ.get(
        "GANGMU_BENCH_CACHE", str(Path.home() / ".cache" / "gangmu-bench")))
    p.add_argument("--gangmu-src", help="gangmu checkout, for the build recipe of binary cases")
    p.add_argument("-o", "--output", help="write OUTPUT.md and OUTPUT.json")
    p.add_argument("--no-fail", action="store_true")
    args = p.parse_args(argv)
    report_tool()

    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)
    rows = []
    installed = available_rules(args.rules)
    builder = None
    for case in load_cases(args.case):
        if "copies" in case:
            rows.extend(run_sdk(case, cache, args.rules, installed))
            continue
        needed = case.get("requires", case["expect"]["rule"])
        reason = f"rule {needed} not installed" if needed not in installed else ""
        if not reason and "binary" in case:
            builder = builder or find_builder(args.gangmu_src)
            if builder is None:
                reason = "no gangmu checkout for the build recipe (--gangmu-src)"
            elif shutil.which(builder.TARGETS[case["binary"].get("target", "arm")]["cc"]) is None:
                reason = f"cross compiler for {case['binary'].get('target', 'arm')} not installed"
        source = None
        if not reason and "binary" not in case:
            try:
                source = fetch(case, cache)
            except FetchError as exc:
                reason = str(exc)
        if reason:
            for variant in case.get("variants", ["pristine"]):
                name = ("pristine" if variant == "pristine" else
                        "touched" if variant == "touch" else "stripped")
                rows.append({
                    "case": case["id"], "variant": name,
                    "truth": str(case["expect"]["version"]),
                    "expected_rule": case["expect"]["rule"], "rule": None,
                    "reported": None, "confidence": None, "verdict": "skipped",
                    "directory": None, "other_findings": 0, "others": [], "seconds": 0.0,
                })
                print(f"skipped  {case['id']:22s} {name:9s} "
                      f"{reason}", flush=True)
            continue
        if source is None:
            source = fetch(case, cache)
        with tempfile.TemporaryDirectory(prefix="gangmu-bench-") as tmp:
            for variant in case.get("variants", ["pristine"]):
                if "binary" in case:
                    name = f"{case['binary'].get('target', 'arm')}-{case['binary'].get('opt', 'Os')}"
                    root = build_image(case, source, Path(tmp) / case["id"], builder)
                    where = "firmware.elf"
                else:
                    name, root = prepare(component_root(case, source),
                                         Path(tmp) / case["id"], variant)
                    where = NEUTRAL
                findings, seconds = scan(root, args.rules)
                verdict, finding = grade(findings, case["expect"], where)
                verdict = known(verdict, finding and finding.get("version"), case["expect"], name)
                others = extras(findings, finding, case["expect"])
                row = {
                    "case": case["id"], "variant": name,
                    "truth": str(case["expect"]["version"]),
                    "expected_rule": case["expect"]["rule"],
                    "rule": finding and finding.get("rule_id"),
                    "reported": finding and finding.get("version"),
                    "confidence": finding and finding.get("confidence"),
                    "verdict": verdict,
                    "directory": finding and finding.get("directory"),
                    "other_findings": len(others),
                    "others": others,
                    "seconds": round(seconds, 2),
                }
                rows.append(row)
                print(f"{verdict:8s} {case['id']:22s} {name:9s} "
                      f"reported {row['reported']} ({row['rule']})", flush=True)
                for o in others:
                    if o["kind"] == "unexpected":
                        print(f"         false positive: {o['rule']} {o['version']} "
                              f"at {o['directory']}", flush=True)

    counts = {v: sum(r["verdict"] == v for r in rows)
              for v in ("exact", "range", "identified", "known", "wrong", "missing", "skipped")}
    kinds = ("bundled", "declared", "duplicate", "unexpected")
    other = {k: sum(o["kind"] == k for r in rows for o in r["others"]) for k in kinds}
    reported = sum(r["verdict"] in ("exact", "range", "identified", "known", "wrong") for r in rows) + sum(
        other[k] for k in ("bundled", "unexpected"))
    counts["false_positive"] = other["unexpected"]
    print("\n" + ", ".join(f"{v} {n}" for v, n in counts.items()))
    print("other findings: " + ", ".join(f"{k} {n}" for k, n in other.items())
          + f"; components reported {reported}, of them false {other['unexpected']}")
    if args.output:
        meta = tool_versions()
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.with_suffix(".json").write_text(json.dumps(
            {"versions": meta, "counts": counts, "other_findings": other,
             "components_reported": reported, "rows": rows}, indent=2) + "\n")
        lines = [f"# Benchmark results", "",
                 f"{meta['gangmu']}; rules: {meta['rules']}", "",
                 "| case | variant | truth | reported | rule | verdict | other findings |",
                 "| --- | --- | --- | --- | --- | --- | --- |"]
        lines += [f"| {r['case']} | {r['variant']} | {r['truth']} | {r['reported'] or '-'} "
                  f"| {r['rule'] or '-'} | {r['verdict']} | {_others(r['others'])} |"
                  for r in rows]
        lines += ["", ", ".join(f"**{v.replace('_', ' ')}** {n}" for v, n in counts.items()),
                  "", "Other findings: " + ", ".join(f"{k} {n}" for k, n in other.items())
                  + f". Of {reported} components reported (graded ones and every other"
                  f" code or binary finding), {other['unexpected']} are false positives.", ""]
        out.with_suffix(".md").write_text("\n".join(lines))
    # a skipped case is not a failure; a false positive is
    failed = counts["wrong"] + counts["missing"] + counts["false_positive"]
    return 0 if (failed == 0 or args.no_fail) else 1


def _others(others: List[dict]) -> str:
    if not others:
        return "-"
    return "; ".join(f"{o['kind']}: {o['rule']} {o['version'] or ''}".rstrip() for o in others)


if __name__ == "__main__":
    sys.exit(main())
