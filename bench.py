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

Clones are cached under ~/.cache/gangmu-bench (or --cache).
"""

from __future__ import annotations

import argparse
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


def fetch(case: dict, cache: Path) -> Path:
    """A checkout of the case's ref, without .git, cached by URL and ref."""
    key = re.sub(r"[^A-Za-z0-9._-]+", "_", f"{case['git']}@{case['ref']}")
    dest = cache / key
    if (dest / ".complete").exists():
        return dest
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    git = ["git", "-c", "advice.detachedHead=false"]
    subprocess.run(git + ["init", "-q", str(dest)], check=True)
    subprocess.run(git + ["-C", str(dest), "fetch", "-q", "--depth", "1",
                          case["git"], case["ref"]], check=True)
    subprocess.run(git + ["-C", str(dest), "checkout", "-q", "FETCH_HEAD"], check=True)
    shutil.rmtree(dest / ".git")
    (dest / ".complete").write_text(case["ref"])
    return dest


def prepare(source: Path, work: Path, variant) -> Tuple[str, Path]:
    name = "pristine" if variant == "pristine" else "stripped"
    root = work / name
    tree = root / NEUTRAL
    shutil.copytree(source, tree, ignore=shutil.ignore_patterns(".complete"))
    if isinstance(variant, dict):
        for rel in variant.get("strip", []):
            target = tree / rel
            if not target.exists():
                raise SystemExit(f"strip: {rel} does not exist in {source}")
            target.unlink()
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


def grade(findings: List[dict], expect: dict) -> Tuple[str, Optional[dict]]:
    # The component may be found at the copy's root or in a subdirectory of it
    # (TinyCrypt's sources sit in lib/); the shallowest, most confident wins.
    here = [f for f in findings if f.get("directory") == NEUTRAL
            or str(f.get("directory", "")).startswith(NEUTRAL + "/")]
    if not here:
        return "missing", None
    finding = min(here, key=lambda f: (f["directory"].count("/"),
                                       -(f.get("confidence") or 0)))
    if finding.get("rule_id") != expect["rule"]:
        return "wrong", finding
    reported, truth = str(finding.get("version") or ""), str(expect["version"])
    if reported == truth:
        return "exact", finding
    if "~" in reported:
        low, high = reported.split("~", 1)
        if _le(low, truth) and _le(truth, high):
            return "range", finding
    return "wrong", finding


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
    return {"gangmu": out, "rules": "; ".join(roots)}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--case", action="append", default=[])
    p.add_argument("--rules", action="append", default=[])
    p.add_argument("--cache", default=os.environ.get(
        "GANGMU_BENCH_CACHE", str(Path.home() / ".cache" / "gangmu-bench")))
    p.add_argument("-o", "--output", help="write OUTPUT.md and OUTPUT.json")
    p.add_argument("--no-fail", action="store_true")
    args = p.parse_args(argv)

    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)
    rows = []
    installed = available_rules(args.rules)
    for case in load_cases(args.case):
        if case["expect"]["rule"] not in installed:
            for variant in case.get("variants", ["pristine"]):
                name = "pristine" if variant == "pristine" else "stripped"
                rows.append({
                    "case": case["id"], "variant": name,
                    "truth": str(case["expect"]["version"]),
                    "expected_rule": case["expect"]["rule"], "rule": None,
                    "reported": None, "confidence": None, "verdict": "skipped",
                    "directory": None, "other_findings": 0, "seconds": 0.0,
                })
                print(f"skipped  {case['id']:22s} {name:9s} "
                      f"rule {case['expect']['rule']} not installed", flush=True)
            continue
        source = fetch(case, cache)
        with tempfile.TemporaryDirectory(prefix="gangmu-bench-") as tmp:
            for variant in case.get("variants", ["pristine"]):
                name, root = prepare(source, Path(tmp) / case["id"], variant)
                findings, seconds = scan(root, args.rules)
                verdict, finding = grade(findings, case["expect"])
                row = {
                    "case": case["id"], "variant": name,
                    "truth": str(case["expect"]["version"]),
                    "expected_rule": case["expect"]["rule"],
                    "rule": finding and finding.get("rule_id"),
                    "reported": finding and finding.get("version"),
                    "confidence": finding and finding.get("confidence"),
                    "verdict": verdict,
                    "directory": finding and finding.get("directory"),
                    "other_findings": len(findings) - (1 if finding else 0),
                    "seconds": round(seconds, 2),
                }
                rows.append(row)
                print(f"{verdict:8s} {case['id']:22s} {name:9s} "
                      f"reported {row['reported']} ({row['rule']})", flush=True)

    counts = {v: sum(r["verdict"] == v for r in rows)
              for v in ("exact", "range", "wrong", "missing", "skipped")}
    print("\n" + ", ".join(f"{v} {n}" for v, n in counts.items()))
    if args.output:
        meta = tool_versions()
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.with_suffix(".json").write_text(json.dumps(
            {"versions": meta, "counts": counts, "rows": rows}, indent=2) + "\n")
        lines = [f"# Benchmark results", "",
                 f"{meta['gangmu']}; rules: {meta['rules']}", "",
                 "| case | variant | truth | reported | rule | verdict |",
                 "| --- | --- | --- | --- | --- | --- |"]
        lines += [f"| {r['case']} | {r['variant']} | {r['truth']} | {r['reported'] or '-'} "
                  f"| {r['rule'] or '-'} | {r['verdict']} |" for r in rows]
        lines += ["", ", ".join(f"**{v}** {n}" for v, n in counts.items()), ""]
        out.with_suffix(".md").write_text("\n".join(lines))
    failed = counts["wrong"] + counts["missing"]      # a skipped case is not a failure
    return 0 if (failed == 0 or args.no_fail) else 1


if __name__ == "__main__":
    sys.exit(main())
