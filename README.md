# 纲目评测基准 · gangmu-bench

[English](README.en.md) · [纲目](https://github.com/GANGMU-SBOM/gangmu) · [免费规则库](https://github.com/GANGMU-SBOM/gangmu-rules)

用真实的上游发布版和芯片 SDK，检验[纲目](https://github.com/GANGMU-SBOM/gangmu)能不能认对组件和版本。
每个用例固定一棵真实的源码树（git 地址 + 标签或提交）以及正确答案；运行时把它拷到一个中性的目录名下，
可选地删掉版本文件，用当前安装的纲目和[规则库](https://github.com/GANGMU-SBOM/gangmu-rules)扫描，再逐条评分：

| 结果 | 含义 |
| --- | --- |
| exact | 报告的版本就是真实版本 |
| range | 报告的是一个包含真实版本的区间（这些版本的函数完全相同，无法再细分） |
| wrong | 认成了别的组件，或者版本区间不包含真实版本 |
| missing | 这个目录什么都没报 |
| skipped | 用例要求的规则没装（比如你没加载某个规则包），不评分，也不算失败 |

现有 SBOM 评测（sbomify、sbombenchmark.dev）都只覆盖有锁文件的语言生态，没有 C/C++ 和嵌入式。
这里的每个数字都能由任何人复现。

## 运行

```bash
pip install gangmu-sbom pyyaml          # 会一并装上免费的 gangmu-rules
python bench.py                          # 全部用例；要的规则没装的用例标为 skipped
python bench.py --case lwip-2.2.0        # 单个用例
python bench.py --rules my-rules/ -o results/mine   # 叠加自己的规则，写出 .md 和 .json
```

全部 9 个用例都只用免费规则库，开箱即评分。

源码缓存在 `~/.cache/gangmu-bench`。最近一次结果见 [results/latest.md](results/latest.md)（任何人可复现，13 行全部评分：9 exact、4 range，0 错 0 漏）。

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
