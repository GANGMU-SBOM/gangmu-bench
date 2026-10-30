# Benchmark results

gangmu-sbom 0.15.0; rules: community 2026.10.29 (pack:community)

| case | variant | truth | reported | rule | verdict |
| --- | --- | --- | --- | --- | --- |
| littlefs-2.4.0-riscv32 | riscv32-O2 | 2.4.0 | 2.0.4~2.11.0 | binary/littlefs | range |
| mbedtls-3.4.0-riscv32 | riscv32-O2 | 3.4.0 | 3.4.0 | binary/mbedtls | exact |
| nghttp2-1.44.0 | pristine | 1.44.0 | 1.44.0 | generic/nghttp2 | exact |
| nghttp2-1.64.0 | pristine | 1.64.0 | 1.64.0 | generic/nghttp2 | exact |
| libwebsockets-4.1.4 | pristine | 4.1.4 | 4.1.4 | generic/libwebsockets | exact |
| libwebsockets-4.3.3 | pristine | 4.3.3 | 4.3.3 | generic/libwebsockets | exact |
| open62541-1.4.4 | pristine | 1.4.4 | 1.4.4 | generic/open62541 | exact |
| paho-mqtt-c-1.3.5 | pristine | 1.3.5 | 1.3.5 | generic/paho-mqtt-c | exact |
| hostap-2.10 | pristine | 2.10 | 2.10 | generic/hostap | exact |
| soem-1.4.0 | pristine | 1.4.0 | 1.4.0 | generic/soem | exact |
| canopennode-4.0 | pristine | 4.0 | 4.0 | generic/canopennode | exact |
| canopennode-2.0 | pristine | 2.0 | 2.0 | generic/canopennode | exact |
| freertos-kernel-10.4.4 | pristine | 10.4.4 | 10.4.4 | generic/freertos-kernel | exact |
| zlib-1.3.1 | pristine | 1.3.1 | 1.3.1 | generic/zlib | exact |
| mbedtls-2.28.10 | pristine | 2.28.10 | 2.28.10 | generic/mbedtls | exact |
| mbedtls-2.28.10 | stripped | 2.28.10 | 2.28.10 | generic/mbedtls | exact |
| mbedtls-3.6.4 | pristine | 3.6.4 | 3.6.4 | generic/mbedtls | exact |
| mbedtls-3.6.4 | stripped | 3.6.4 | 3.6.4 | generic/mbedtls | exact |
| littlefs-2.9.1 | pristine | 2.9.1 | 2.9.1 | generic/littlefs | exact |
| littlefs-2.11.3 | pristine | 2.11.3 | 2.11.3 | generic/littlefs | exact |
| tinycrypt-0.2.8 | pristine | 0.2.8 | 0.2.8 | generic/tinycrypt | exact |
| lwip-2.2.0 | pristine | 2.2.0 | 2.2.0 | generic/lwip | exact |
| lwip-2.1.3 | pristine | 2.1.3 | 2.1.3 | generic/lwip | exact |
| libcoap-4.3.4 | pristine | 4.3.4 | 4.3.4 | generic/libcoap | exact |
| libcoap-4.3.4 | stripped | 4.3.4 | 4.3.4 | generic/libcoap | exact |
| lvgl-8.3.11 | pristine | 8.3.11 | 8.3.11 | generic/lvgl | exact |
| lvgl-8.3.11 | stripped | 8.3.11 | 8.3.11 | generic/lvgl | exact |

**exact** 26, **range** 1, **wrong** 0, **missing** 0, **skipped** 0
