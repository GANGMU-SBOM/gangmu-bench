# gangmu-bench

[![bench](https://github.com/GANGMU-SBOM/gangmu-bench/actions/workflows/bench.yml/badge.svg?branch=main)](https://github.com/GANGMU-SBOM/gangmu-bench/actions/workflows/bench.yml)

[中文](README.md) · [Gangmu](https://github.com/GANGMU-SBOM/gangmu) · [free rule base](https://github.com/GANGMU-SBOM/gangmu-rules)

**Does [Gangmu](https://github.com/GANGMU-SBOM/gangmu) recognise the right component and version in real upstream
releases and chip-vendor SDKs?** Each case pins a real source tree (git URL plus tag or commit) and the correct
answer. The runner copies it under a neutral directory name, optionally deletes the version files, scans it with the
installed tool and [rule base](https://github.com/GANGMU-SBOM/gangmu-rules), and grades each case:

| Result | Meaning |
| --- | --- |
| exact | the reported version is the true version |
| range | the reported range contains the true version (those versions have identical functions) |
| identified | the right component; the copy states no version of its own, so the version cannot be checked (vendor-SDK copies only) |
| known | a wrong answer the case records as understood (`expect.known` with `known_why`): the vendor's or upstream's own statement is off and the tool reports what the code is. Listed in the results, not a failure; any other wrong answer still is |
| wrong | another component, or a range that excludes the true version |
| missing | nothing was reported for the directory |
| skipped | the case expects a rule that is not installed (for example a rule pack you did not load); not graded, not a failure |

Every other finding the scan makes in the tree is listed and labelled too, so **false positives** count against the score:

| label | meaning |
| --- | --- |
| duplicate | the same rule reported again in this tree |
| declared | a dependency a manifest in the tree declares (CMake, Bazel, Arduino ...), not a code identification |
| bundled | a component the case says this release really carries (`bundled:`, each one checked by hand) |
| unexpected | none of these: a **false positive**, a failure like `wrong` or `missing` |

Existing SBOM benchmarks only cover ecosystems with lock files; none covers C/C++ or embedded. Every number here can
be reproduced by anyone.

## Run

```bash
pip install gangmu-sbom pyyaml          # pulls in the free gangmu-rules
python bench.py                          # all cases; cases whose rule is not installed are skipped
python bench.py --case lwip-2.2.0        # one case
python bench.py --rules my-rules/ -o results/mine   # add your own rules, write .md and .json
```

It starts by printing the path and version of the `gangmu` it measures (the first one on PATH) and the rule roots it loads, and warns when that gangmu is not in the Python environment running `bench.py`. To measure a virtual environment's gangmu, put its `bin` first on PATH. The result `.json` records the path as `versions.gangmu_path`.

All 139 cases use only the free rule base: 130 upstream release trees (each pinned to a tag or commit) and 9 vendor SDKs (pinned commits, 57 copies). 137 are graded out of the box; the 2 firmware-image cases need a cross compiler, capstone and the gangmu sources, and are marked skipped without them.

Every run computes and records four numbers: **recall** (expected components found by the right rule, whatever the version), **precision** (reported components that are really there; the denominator is the graded components plus every other code or binary finding in the tree, each checked by hand and either recorded in the case as `bundled:` or counted as a false positive; manifest-declared dependencies are listed but not counted), **version exact** and **version exact or a range containing it** (over the found components whose truth is known).

Sources are cached in `~/.cache/gangmu-bench`. Latest results: [results/latest.md](results/latest.md) (2026-10-31, gangmu 0.15.0 plus GANGMU-SBOM/gangmu#157, rules 2026.10.29; anyone can reproduce them): 264 rows graded, **recall 100%** (264/264), **precision 100%** (0 false positives among the 329 components reported; 65 more are components these trees really carry, each checked, and 48 are manifest-declared dependencies), version exact 89.8%, exact or a range containing it 98.8%. 230 exact, 23 ranges containing the truth, 8 identified (the copy states no version), and 3 known: two TinyCrypt copies that say 0.2.7 but carry 0.2.8's fixes, reported as 0.2.8, and libwebsockets' v4.0.21 tag, whose `CMakeLists.txt` already says 4.0.22.

## Cases

A `touch` variant appends a comment line to every `.c`/`.h` file, which breaks every byte-for-byte anchor and file-set hash, so only functions can decide.

Where a release really carries another component (zstd bundles xxhash), list those rule ids under `bundled:` and they do not count as false positives; check each against the source before adding it.

A vendor-SDK case has a `copies:` list: the pinned SDK is scanned once, whole and under its own name (that is how a vendor ships it), and each listed copy is graded at its own path against the version the vendor wrote in its own header; the SDK's other findings are labelled against the SDK-level `bundled:`.

Firmware-image cases (`cases/firmware-images.yaml`) carry a `binary:` block: the pinned tree is cross-compiled (library code only, stripped, no libc, RISC-V rv32imac) and the one ELF is scanned and graded the same way. The releases are deliberately not among those the rule's fingerprints were built from, so the answer must come from neighbouring releases, not from a copy of the same build. Needs `riscv64-unknown-elf-gcc`, `pip install "gangmu-sbom[disasm]"` (capstone) and a gangmu checkout (`--gangmu-src`, for the build recipe in `benchmarks/binary/build_corpus.py`); without them the case is skipped.

`cases/*.yaml`; contributions welcome, especially real copies inside vendor SDKs: give the SDK repository, a pinned
commit, the component directory and the version the vendor declares. A `wrong` case is as valuable as an `exact` one:
it becomes a fix in the rule base.

## Related repositories

- [gangmu](https://github.com/GANGMU-SBOM/gangmu): the tool under test; `docs/BENCHMARK.md` there holds the analysis.
  Its performance baseline (`gangmu perf`) stays there and is checked on every PR.
- [gangmu-rules](https://github.com/GANGMU-SBOM/gangmu-rules): the free rules under test. File `wrong` or `missing`
  results there with the case id.

## Contribute, get in touch

- **Add benchmark cases** (especially real copies inside Chinese chip SDKs): open an issue or pull request.
- **Want to take on an SDK, or have real firmware samples to help verify:** contact me first so we do not duplicate work.
- **Technical consulting, business enquiries, commercial rule packs:** contact me as well.

Email 64031875@qq.com, or join the WeChat "CRA compliance group" (the QR code expires; email if it does not scan).

<img src="docs/assets/cra-wechat-group.png" alt="WeChat group QR code" width="200">

## Licence

Apache-2.0. Cases record upstream addresses and versions only, no third-party source.
