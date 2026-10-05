# 贡献用例 · Contributing a case

欢迎补充评测用例，尤其是芯片厂商 SDK 和国内常见的开源组件。Cases for chip-vendor SDKs and components common in the
Chinese ecosystem are especially welcome.

1. Add an entry to `cases/upstream-releases.yaml`: a public git URL, a **pinned tag or commit**, and the expected
   component and version. Do not add trees that cannot be redistributed or reproduced by anyone.
2. Run it locally:

   ```bash
   pip install gangmu-sbom pyyaml
   python bench.py
   ```

3. If the result is `wrong` or `missing`, that is a finding, not a failure of your case. Keep it and open an issue in
   [gangmu-rules](https://github.com/GANGMU-SBOM/gangmu-rules) (or [gangmu](https://github.com/GANGMU-SBOM/gangmu) if the
   scanner is at fault).
4. Regenerate `results/latest.json` and `results/latest.md` with `python bench.py` and include them in the pull request.

Sign off every commit (`git commit -s`, the [DCO](https://developercertificate.org/)). Questions: 64031875@qq.com.
