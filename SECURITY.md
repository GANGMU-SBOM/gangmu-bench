# 安全政策 · Security Policy

[English below](#english)

## 报告安全问题

本仓库只包含评测脚本、用例清单和评测结果，不包含需要部署的服务。如果你发现 `bench.py` 存在安全问题
（例如处理用例时的命令注入、路径穿越），请**不要**公开提 issue，而是通过本仓库的
[私密漏洞报告](https://github.com/GANGMU-SBOM/gangmu-bench/security/advisories/new)提交。
我们会在 5 个工作日内确认收到，并与你协调修复和公开的时间。

扫描工具本身的漏洞请报到 [gangmu](https://github.com/GANGMU-SBOM/gangmu/security/advisories/new)。
评测结果与事实不符（识别错误的版本或组件）请直接提 issue 并附上可复现的上游版本。

## 支持的版本

只有最新的版本会收到修复。

---

## English

This repository holds the benchmark runner, the case list and the published results; there is no deployed service.
**Security problems in `bench.py`** (for example command injection or path traversal while handling a case): please do
not open a public issue. Use this repository's
[private vulnerability reporting](https://github.com/GANGMU-SBOM/gangmu-bench/security/advisories/new). We acknowledge
within five working days and coordinate a fix and disclosure date with you.

Vulnerabilities in the scanner itself go to
[gangmu](https://github.com/GANGMU-SBOM/gangmu/security/advisories/new). A published result that is factually wrong
(a misidentified component or version) can be reported publicly with a reproducible upstream release.

**Supported versions:** only the latest version receives fixes.
