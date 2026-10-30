# 纲目评测基准 · gangmu-bench

[![bench](https://github.com/GANGMU-SBOM/gangmu-bench/actions/workflows/bench.yml/badge.svg?branch=main)](https://github.com/GANGMU-SBOM/gangmu-bench/actions/workflows/bench.yml)

[English](README.en.md) · [纲目](https://github.com/GANGMU-SBOM/gangmu) · [免费规则库](https://github.com/GANGMU-SBOM/gangmu-rules)

用真实的上游发布版和芯片 SDK，检验[纲目](https://github.com/GANGMU-SBOM/gangmu)能不能认对组件和版本。
每个用例固定一棵真实的源码树（git 地址 + 标签或提交）以及正确答案；运行时把它拷到一个中性的目录名下，
可选地删掉版本文件，用当前安装的纲目和[规则库](https://github.com/GANGMU-SBOM/gangmu-rules)扫描，再逐条评分：

| 结果 | 含义 |
| --- | --- |
| exact | 报告的版本就是真实版本 |
| range | 报告的是一个包含真实版本的区间（这些版本的函数完全相同，无法再细分） |
| identified | 认对了组件；这份副本自己没写版本，无从核对版本（只用于芯片 SDK 里的副本） |
| wrong | 认成了别的组件，或者版本区间不包含真实版本 |
| missing | 这个目录什么都没报 |
| skipped | 用例要求的规则没装（比如你没加载某个规则包），不评分，也不算失败 |

除了被评分的那条结论，扫描在这棵树里报出的其他结论也逐条列出并归类，这样**误报**也算进成绩：

| 归类 | 含义 |
| --- | --- |
| duplicate | 同一条规则在这棵树里又报了一次 |
| declared | 树里的清单文件（CMake、Bazel、Arduino……）声明的依赖，不是代码识别 |
| bundled | 用例写明这个发布版确实带着的组件（`bundled:`，逐条人工核对过） |
| unexpected | 以上都不是：**误报**，和 `wrong`、`missing` 一样算失败 |

现有 SBOM 评测（sbomify、sbombenchmark.dev）都只覆盖有锁文件的语言生态，没有 C/C++ 和嵌入式。
这里的每个数字都能由任何人复现。

## 运行

```bash
pip install gangmu-sbom pyyaml          # 会一并装上免费的 gangmu-rules
python bench.py                          # 全部用例；要的规则没装的用例标为 skipped
python bench.py --case lwip-2.2.0        # 单个用例
python bench.py --rules my-rules/ -o results/mine   # 叠加自己的规则，写出 .md 和 .json
```

开始时会打印实际被测的 `gangmu`（PATH 里的第一个）的路径和版本，以及加载的规则库；它不在运行 `bench.py` 的 Python 环境里时会警告。想测某个虚拟环境里的版本，就把它的 `bin` 放到 PATH 最前面。结果的 `.json` 里记录了路径（`versions.gangmu_path`）。

全部 23 个用例都只用免费规则库；其中 21 个开箱即评分，2 个固件镜像用例需要交叉编译器、capstone 和纲目源码，缺时标为 skipped。

源码缓存在 `~/.cache/gangmu-bench`。最近一次结果见 [results/latest.md](results/latest.md)（用 gangmu-sbom 0.15.0 和规则库 2026.10.29 跑的；任何人可复现，27 行全部评分：26 exact、1 range，0 错 0 漏。唯一的 range 是 littlefs 2.4.0 的 RISC-V 固件镜像，报 `2.0.4~2.11.0`）。

## 用例

`cases/*.yaml`，每条：

```yaml
- id: mbedtls-3.6.4
  git: https://github.com/Mbed-TLS/mbedtls
  ref: mbedtls-3.6.4                     # 标签或提交，不能是分支
  expect: {rule: generic/mbedtls, version: 3.6.4}
  variants:
    - pristine                           # 原样
    - strip: [include/mbedtls/version.h, include/mbedtls/build_info.h]   # 只剩函数能判断
```

变体还有 `touch`：给每个 `.c`/`.h` 末尾追加一行注释，所有逐字节吻合的锚点和文件集哈希都失效，只剩函数能判断。

一个发布版里确实带着别的组件（比如 OpenSSL 1.1.x 里没有，zstd 里带 xxhash）时，用 `bundled:` 列出这些规则 id，它们就不算误报；每一条都要核对过源码再加。

芯片 SDK 用例带 `copies:` 列表：固定的 SDK 整棵扫一遍（不改名，厂商就是这样发布的），列表里每份副本在自己的路径上按厂商自己头文件里写的版本评分；SDK 里其余的结论按 SDK 级的 `bundled:` 归类。

固件镜像用例（`cases/firmware-images.yaml`）带一个 `binary:` 块：把固定的源码树只编译库代码、去符号（RISC-V rv32imac，不链接 libc），
对这一个 ELF 做扫描并评分。所选发布版刻意不在规则的指纹发布版之列，所以答案只能来自相邻版本的函数，而不是同一份构建。
需要 `riscv64-unknown-elf-gcc`、`pip install "gangmu-sbom[disasm]"`（capstone）和纲目源码（`--gangmu-src`，取其 `benchmarks/binary/build_corpus.py` 的构建方法）；缺编译器或源码时该用例标为 skipped。

欢迎补充用例，尤其是国产芯片 SDK 里的真实副本：写明 SDK 仓库、固定的提交、组件所在目录和厂商自己声明的版本。
一个 `wrong` 的用例和一个 `exact` 的用例同样有价值，它会变成规则库的修复。

## 与其他仓库的关系

- [gangmu](https://github.com/GANGMU-SBOM/gangmu) 是被测的工具；[gangmu-rules](https://github.com/GANGMU-SBOM/gangmu-rules) 是被测的免费规则。`wrong` 或 `missing` 的结果，去规则库提 issue 并附上用例 id；工具本身的错误去工具仓库。
- 工具仓库的 `docs/BENCHMARK.md` 是结果和分析；这里是可以重跑的用例和脚本。
- 工具仓库的性能基线（`gangmu perf`）留在工具仓库，每个 PR 都会检查；这里的评测按周运行，量的是准确率。

## 参与共建，联系我们

- **补评测用例**（尤其是国产芯片 SDK 里的真实副本）：直接提 issue 或 PR；
- **想认领某个 SDK、手上有真实固件样本愿意帮忙验证**：先联系我，避免重复劳动；
- **技术咨询、商务合作、商业版规则包**：同样联系我。

邮箱 64031875@qq.com，或扫码进「CRA 合规群」（二维码有有效期，扫不出来请发邮件）。

<img src="docs/assets/cra-wechat-group.png" alt="CRA 合规群二维码" width="200">

## 许可证

Apache-2.0。用例只记录上游地址和版本，不包含任何第三方源码。
