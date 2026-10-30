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
| wrong | another component, or a range that excludes the true version |
| missing | nothing was reported for the directory |
| skipped | the case expects a rule that is not installed (for example a rule pack you did not load); not graded, not a failure |

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

All 23 cases use only the free rule base; 21 are graded out of the box, and the 2 firmware-image cases need a cross compiler, capstone and the gangmu sources, and are marked skipped without them.

Sources are cached in `~/.cache/gangmu-bench`. Latest results: [results/latest.md](results/latest.md) (run with gangmu-sbom 0.15.0 and rules 2026.10.29; anyone can reproduce it: all 27 rows graded, 26 exact, 1 range, 0 wrong, 0 missing. The one range is the littlefs 2.4.0 RISC-V firmware image, reported as `2.0.4~2.11.0`).

## Cases

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
