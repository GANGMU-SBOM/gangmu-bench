# Benchmark results

gangmu-sbom 0.6.0; rules: community 2026.10.5 (pack:community)

| case | variant | truth | reported | rule | verdict |
| --- | --- | --- | --- | --- | --- |
| mbedtls-2.28.10 | pristine | 2.28.10 | 2.28.10 | generic/mbedtls | exact |
| mbedtls-2.28.10 | stripped | 2.28.10 | 2.28.8~2.28.10 | generic/mbedtls | range |
| mbedtls-3.6.4 | pristine | 3.6.4 | 3.6.4 | generic/mbedtls | exact |
| mbedtls-3.6.4 | stripped | 3.6.4 | 3.6.4~3.6.5 | generic/mbedtls | range |
| littlefs-2.9.1 | pristine | 2.9.1 | 2.9.1 | generic/littlefs | exact |
| littlefs-2.11.3 | pristine | 2.11.3 | 2.11.3 | generic/littlefs | exact |
| tinycrypt-0.2.8 | pristine | 0.2.8 | 0.2.8 | generic/tinycrypt | exact |
| lwip-2.2.0 | pristine | 2.2.0 | 2.2.0 | generic/lwip | exact |
| lwip-2.1.3 | pristine | 2.1.3 | 2.1.3 | generic/lwip | exact |
| libcoap-4.3.4 | pristine | 4.3.4 | 4.3.4 | generic/libcoap | exact |
| libcoap-4.3.4 | stripped | 4.3.4 | 4.3.2~4.3.4a | generic/libcoap | range |
| lvgl-8.3.11 | pristine | 8.3.11 | 8.3.11 | generic/lvgl | exact |
| lvgl-8.3.11 | stripped | 8.3.11 | 8.3.11~8.4.0 | generic/lvgl | range |

**exact** 9, **range** 4, **wrong** 0, **missing** 0, **skipped** 0
