# Benchmark results

gangmu-sbom 0.15.0; rules: community 2026.10.29 (pack:community)

| case | variant | truth | reported | rule | verdict | other findings |
| --- | --- | --- | --- | --- | --- | --- |
| littlefs-2.4.0-riscv32 | riscv32-O2 | 2.4.0 | 2.0.4~2.11.0 | binary/littlefs | range | - |
| mbedtls-3.4.0-riscv32 | riscv32-O2 | 3.4.0 | 3.4.0 | binary/mbedtls | exact | - |
| nghttp2-1.44.0 | pristine | 1.44.0 | 1.44.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| nghttp2-1.64.0 | pristine | 1.64.0 | 1.64.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| libwebsockets-4.1.4 | pristine | 4.1.4 | 4.1.4 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| libwebsockets-4.3.3 | pristine | 4.3.3 | 4.3.3 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| open62541-1.4.4 | pristine | 1.4.4 | 1.4.4 | generic/open62541 | exact | - |
| paho-mqtt-c-1.3.5 | pristine | 1.3.5 | 1.3.5 | generic/paho-mqtt-c | exact | - |
| hostap-2.10 | pristine | 2.10 | 2.10 | generic/hostap | exact | - |
| soem-1.4.0 | pristine | 1.4.0 | 1.4.0 | generic/soem | exact | - |
| canopennode-4.0 | pristine | 4.0 | 4.0 | generic/canopennode | exact | - |
| canopennode-2.0 | pristine | 2.0 | 2.0 | generic/canopennode | exact | - |
| freertos-kernel-10.4.4 | pristine | 10.4.4 | 10.4.4 | generic/freertos-kernel | exact | - |
| zlib-1.3.1 | pristine | 1.3.1 | 1.3.1 | generic/zlib | exact | - |
| tencentos-tiny-kernel-2.1.0 | pristine | 2.1.0 | 2.1.0 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.2.0 | pristine | 2.2.0 | 2.2.0 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.2.0 | stripped | 2.2.0 | 2.2.0~2.4.3 | generic/tencentos-tiny-kernel | range | - |
| tencentos-tiny-kernel-2.2.1 | pristine | 2.2.1 | 2.2.1 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.2.1 | stripped | 2.2.1 | 2.2.0~2.4.3 | generic/tencentos-tiny-kernel | range | - |
| tencentos-tiny-kernel-2.3.1 | pristine | 2.3.1 | 2.3.1 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.3.1 | stripped | 2.3.1 | 2.2.0~2.4.3 | generic/tencentos-tiny-kernel | range | - |
| tencentos-tiny-kernel-2.4.0 | pristine | 2.4.0 | 2.4.0 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.4.0 | stripped | 2.4.0 | 2.2.0~2.4.3 | generic/tencentos-tiny-kernel | range | - |
| tencentos-tiny-kernel-2.4.1 | pristine | 2.4.1 | 2.4.1 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.4.1 | stripped | 2.4.1 | 2.2.0~2.4.3 | generic/tencentos-tiny-kernel | range | - |
| tencentos-tiny-kernel-2.4.2 | pristine | 2.4.2 | 2.4.2 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.4.2 | stripped | 2.4.2 | 2.2.0~2.4.3 | generic/tencentos-tiny-kernel | range | - |
| tencentos-tiny-kernel-2.4.3 | pristine | 2.4.3 | 2.4.3 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.4.3 | stripped | 2.4.3 | 2.2.0~2.4.3 | generic/tencentos-tiny-kernel | range | - |
| tencentos-tiny-kernel-2.4.4 | pristine | 2.4.4 | 2.4.4 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.4.4 | stripped | 2.4.4 | 2.4.4 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.4.5 | pristine | 2.4.5 | 2.4.5 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.4.5 | stripped | 2.4.5 | 2.4.5 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.5.0 | pristine | 2.5.0 | 2.5.0 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.5.0 | stripped | 2.5.0 | 2.5.0 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.5.1 | pristine | 2.5.1 | 2.5.1 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.5.1 | stripped | 2.5.1 | 2.5.1~2.5.2 | generic/tencentos-tiny-kernel | range | - |
| tencentos-tiny-kernel-2.5.2 | pristine | 2.5.2 | 2.5.2 | generic/tencentos-tiny-kernel | exact | - |
| tencentos-tiny-kernel-2.5.2 | stripped | 2.5.2 | 2.5.1~2.5.2 | generic/tencentos-tiny-kernel | range | - |
| nghttp2-1.20.0 | pristine | 1.20.0 | 1.20.0 | generic/nghttp2 | exact | bundled: generic/http-parser 2.7.1 |
| nghttp2-1.20.0 | stripped | 1.20.0 | 1.20.0 | generic/nghttp2 | exact | bundled: generic/http-parser 2.7.1 |
| nghttp2-1.40.0 | pristine | 1.40.0 | 1.40.0 | generic/nghttp2 | exact | - |
| nghttp2-1.40.0 | stripped | 1.40.0 | 1.40.0 | generic/nghttp2 | exact | - |
| nghttp2-1.52.0 | pristine | 1.52.0 | 1.52.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| nghttp2-1.52.0 | stripped | 1.52.0 | 1.50.0~1.52.0 | generic/nghttp2 | range | bundled: generic/llhttp |
| nghttp2-1.59.0 | pristine | 1.59.0 | 1.59.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| nghttp2-1.59.0 | stripped | 1.59.0 | 1.59.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| nghttp2-1.66.0 | pristine | 1.66.0 | 1.66.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| nghttp2-1.66.0 | stripped | 1.66.0 | 1.66.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| nghttp2-1.70.0 | pristine | 1.70.0 | 1.70.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| nghttp2-1.70.0 | stripped | 1.70.0 | 1.70.0 | generic/nghttp2 | exact | bundled: generic/llhttp |
| libwebsockets-3.0.1 | pristine | 3.0.1 | 3.0.1 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| libwebsockets-3.0.1 | stripped | 3.0.1 | 3.0.1 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| libwebsockets-3.2.2 | pristine | 3.2.2 | 3.2.2 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| libwebsockets-3.2.2 | stripped | 3.2.2 | 3.2.2 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| libwebsockets-4.0.21 | pristine | 4.0.21 | 4.0.22 | generic/libwebsockets | wrong | bundled: generic/zlib 1.2.5 |
| libwebsockets-4.0.21 | stripped | 4.0.21 | 4.0.21 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| libwebsockets-4.1.6 | pristine | 4.1.6 | 4.1.6 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| libwebsockets-4.1.6 | stripped | 4.1.6 | 4.1.6 | generic/libwebsockets | exact | bundled: generic/zlib 1.2.5 |
| libwebsockets-4.5.8 | pristine | 4.5.8 | 4.5.8 | generic/libwebsockets | exact | bundled: generic/cmsis5-core 5.5.0~5.6.0; bundled: generic/zlib 1.2.5; declared: declared/cmake/pico_sdk |
| libwebsockets-4.5.8 | stripped | 4.5.8 | 4.5.8 | generic/libwebsockets | exact | bundled: generic/cmsis5-core 5.5.0~5.6.0; bundled: generic/zlib 1.2.5; declared: declared/cmake/pico_sdk |
| paho-mqtt-c-1.1.0 | pristine | 1.1.0 | 1.1.0 | generic/paho-mqtt-c | exact | - |
| paho-mqtt-c-1.1.0 | stripped | 1.1.0 | 1.1.0 | generic/paho-mqtt-c | exact | - |
| paho-mqtt-c-1.3.1 | pristine | 1.3.1 | 1.3.1 | generic/paho-mqtt-c | exact | declared: declared/conan/OpenSSL 1.0.2n |
| paho-mqtt-c-1.3.1 | stripped | 1.3.1 | 1.3.1 | generic/paho-mqtt-c | exact | declared: declared/conan/OpenSSL 1.0.2n |
| paho-mqtt-c-1.3.11 | pristine | 1.3.11 | 1.3.11 | generic/paho-mqtt-c | exact | - |
| paho-mqtt-c-1.3.11 | stripped | 1.3.11 | 1.3.11 | generic/paho-mqtt-c | exact | - |
| paho-mqtt-c-1.3.14 | pristine | 1.3.14 | 1.3.14 | generic/paho-mqtt-c | exact | - |
| paho-mqtt-c-1.3.14 | stripped | 1.3.14 | 1.3.14 | generic/paho-mqtt-c | exact | - |
| paho-mqtt-c-1.3.16 | pristine | 1.3.16 | 1.3.16 | generic/paho-mqtt-c | exact | - |
| paho-mqtt-c-1.3.16 | stripped | 1.3.16 | 1.3.16 | generic/paho-mqtt-c | exact | - |
| openthread-2026.06.0 | pristine | 2026.06.0 | 2026.06.0 | generic/openthread | exact | - |
| openthread-2026.07.0 | pristine | 2026.07.0 | 2026.07.0 | generic/openthread | exact | - |
| openthread-2026.08.0 | pristine | 2026.08.0 | 2026.08.0 | generic/openthread | exact | - |
| openthread-2026.09.0 | pristine | 2026.09.0 | 2026.09.0 | generic/openthread | exact | - |
| openthread-2026.10.0 | pristine | 2026.10.0 | 2026.10.0 | generic/openthread | exact | - |
| openthread-20191113 | pristine | 20191113 | 20191113 | generic/openthread | exact | bundled: generic/mbedtls 2.14.0; bundled: binary/mbedtls 2.16.2 |
| openthread-20200818 | pristine | 20200818 | 20200818 | generic/openthread | exact | bundled: generic/mbedtls 2.14.0; bundled: binary/mbedtls 2.16.3 |
| openthread-20221027 | pristine | 20221027 | 20221027 | generic/openthread | exact | bundled: generic/mbedtls 2.28.0 |
| openthread-20230119 | pristine | 20230119 | 20230119 | generic/openthread | exact | bundled: generic/mbedtls 2.28.0 |
| openthread-20230706 | pristine | 20230706 | 20230706 | generic/openthread | exact | bundled: generic/mbedtls 2.28.0 |
| openthread-20250612 | pristine | 20250612 | 20250612 | generic/openthread | exact | bundled: generic/mbedtls 3.6.0 |
| aws-iot-device-sdk-c-2.0.0 | pristine | 2.0.0 | 2.0.0 | generic/aws-iot-device-sdk-c | exact | - |
| aws-iot-device-sdk-c-2.2.1 | pristine | 2.2.1 | 2.2.1 | generic/aws-iot-device-sdk-c | exact | bundled: generic/jsmn 1.0.0 |
| aws-iot-device-sdk-c-3.0.1 | pristine | 3.0.1 | 3.0.1 | generic/aws-iot-device-sdk-c | exact | bundled: generic/jsmn 1.0.0 |
| aws-iot-device-sdk-c-3.1.0 | pristine | 3.1.0 | 3.1.0~3.1.2 | generic/aws-iot-device-sdk-c | range | bundled: generic/jsmn 1.0.0 |
| aws-iot-device-sdk-c-3.1.5 | pristine | 3.1.5 | 3.1.4~3.1.5 | generic/aws-iot-device-sdk-c | range | bundled: generic/jsmn 1.0.0 |
| alios-things-kernel-1.1.0 | pristine | 1.1.0 | 1.1.0 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-1.1.1 | pristine | 1.1.1 | 1.1.1 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-1.1.2 | pristine | 1.1.2 | 1.1.2 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-1.2.0 | pristine | 1.2.0 | 1.2.0 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-1.2.1 | pristine | 1.2.1 | 1.2.1 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-1.2.2 | pristine | 1.2.2 | 1.2.2 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-1.3.0 | pristine | 1.3.0 | 1.3.0~1.3.3 | generic/alios-things-kernel | range | - |
| alios-things-kernel-1.3.1 | pristine | 1.3.1 | 1.3.0~1.3.3 | generic/alios-things-kernel | range | - |
| alios-things-kernel-1.3.2 | pristine | 1.3.2 | 1.3.2~1.3.3 | generic/alios-things-kernel | range | - |
| alios-things-kernel-1.3.3 | pristine | 1.3.3 | 1.3.3 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-1.3.4 | pristine | 1.3.4 | 1.3.4 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-2.0.0 | pristine | 2.0.0 | 2.0.0 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-2.1.0 | pristine | 2.1.0 | 2.1.0 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-3.0.0 | pristine | 3.0.0 | 3.0.0 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-3.1.0 | pristine | 3.1.0 | 3.1.0 | generic/alios-things-kernel | exact | - |
| alios-things-kernel-3.3.0 | pristine | 3.3.0 | 3.3.0 | generic/alios-things-kernel | exact | - |
| liteos-kernel-5.0.0 | pristine | 5.0.0 | 5.0.0 | generic/liteos-kernel | exact | - |
| liteos-kernel-5.0.0 | touched | 5.0.0 | 5.0.0 | generic/liteos-kernel | exact | - |
| liteos-kernel-5.1.0 | pristine | 5.1.0 | 5.1.0 | generic/liteos-kernel | exact | - |
| liteos-kernel-5.1.0 | touched | 5.1.0 | 5.1.0 | generic/liteos-kernel | exact | - |
| gmssl-2.0.0 | pristine | 2.0.0 | 2.0.0 | generic/gmssl-2 | exact | - |
| gmssl-2.0.0 | stripped | 2.0.0 | 2.0.0 | generic/gmssl-2 | exact | - |
| gmssl-2.3.3 | pristine | 2.3.3 | 2.3.3 | generic/gmssl-2 | exact | - |
| gmssl-2.3.3 | stripped | 2.3.3 | 2.3.3~2.3.4 | generic/gmssl-2 | range | - |
| gmssl-2.4.5 | pristine | 2.4.5 | 2.4.5 | generic/gmssl-2 | exact | - |
| gmssl-2.4.5 | stripped | 2.4.5 | 2.4.5 | generic/gmssl-2 | exact | - |
| gmssl-2.5.0 | pristine | 2.5.0 | 2.5.0 | generic/gmssl-2 | exact | - |
| gmssl-2.5.0 | stripped | 2.5.0 | 2.5.0 | generic/gmssl-2 | exact | - |
| gmssl-2.5.3 | pristine | 2.5.3 | 2.5.3 | generic/gmssl-2 | exact | - |
| gmssl-2.5.3 | stripped | 2.5.3 | 2.5.3 | generic/gmssl-2 | exact | - |
| gmssl-2.5.4 | pristine | 2.5.4 | 2.5.4 | generic/gmssl-2 | exact | - |
| gmssl-2.5.4 | stripped | 2.5.4 | 2.5.4 | generic/gmssl-2 | exact | - |
| gmssl-3.0.0 | pristine | 3.0.0 | 3.0.0 | generic/gmssl | exact | - |
| gmssl-3.0.0 | stripped | 3.0.0 | 3.0.0 | generic/gmssl | exact | - |
| gmssl-3.2.0 | pristine | 3.2.0 | 3.2.0 | generic/gmssl | exact | - |
| gmssl-3.2.0 | stripped | 3.2.0 | 3.2.0 | generic/gmssl | exact | - |
| tongsuo-8.1.3 | pristine | 8.1.3 | 8.1.3 | generic/tongsuo | exact | - |
| tongsuo-8.1.3 | stripped | 8.1.3 | 8.1.3 | generic/tongsuo | exact | - |
| tongsuo-8.2.1 | pristine | 8.2.1 | 8.2.1 | generic/tongsuo | exact | - |
| tongsuo-8.2.1 | stripped | 8.2.1 | 8.2.1 | generic/tongsuo | exact | - |
| tongsuo-8.3.3 | pristine | 8.3.3 | 8.3.3 | generic/tongsuo | exact | - |
| tongsuo-8.3.3 | stripped | 8.3.3 | 8.3.3 | generic/tongsuo | exact | - |
| tongsuo-8.4.0 | pristine | 8.4.0 | 8.4.0 | generic/tongsuo | exact | - |
| tongsuo-8.4.0 | stripped | 8.4.0 | 8.4.0 | generic/tongsuo | exact | - |
| tongsuo-8.5.0 | pristine | 8.5.0 | 8.5.0 | generic/tongsuo | exact | - |
| tongsuo-8.5.0 | stripped | 8.5.0 | 8.5.0 | generic/tongsuo | exact | - |
| openssl-1.1.0g | pristine | 1.1.0g | 1.1.0g | generic/openssl | exact | - |
| openssl-1.1.0g | stripped | 1.1.0g | 1.1.0g | generic/openssl | exact | - |
| openssl-1.1.0l | pristine | 1.1.0l | 1.1.0l | generic/openssl | exact | - |
| openssl-1.1.0l | stripped | 1.1.0l | 1.1.0l | generic/openssl | exact | - |
| openssl-1.1.1k | pristine | 1.1.1k | 1.1.1k | generic/openssl | exact | - |
| openssl-1.1.1k | stripped | 1.1.1k | 1.1.1k | generic/openssl | exact | - |
| openssl-1.1.1w | pristine | 1.1.1w | 1.1.1w | generic/openssl | exact | - |
| openssl-1.1.1w | stripped | 1.1.1w | 1.1.1w | generic/openssl | exact | - |
| openssl-3.0.22 | pristine | 3.0.22 | 3.0.22 | generic/openssl | exact | - |
| openssl-3.0.22 | stripped | 3.0.22 | 3.0.22 | generic/openssl | exact | - |
| openssl-3.5.9 | pristine | 3.5.9 | 3.5.9 | generic/openssl | exact | - |
| openssl-3.5.9 | stripped | 3.5.9 | 3.5.9 | generic/openssl | exact | - |
| mbedtls-2.7.19 | pristine | 2.7.19 | 2.7.19 | generic/mbedtls | exact | - |
| mbedtls-2.7.19 | stripped | 2.7.19 | 2.7.19 | generic/mbedtls | exact | - |
| mbedtls-2.16.12 | pristine | 2.16.12 | 2.16.12 | generic/mbedtls | exact | - |
| mbedtls-2.16.12 | stripped | 2.16.12 | 2.16.12 | generic/mbedtls | exact | - |
| mbedtls-3.1.0 | pristine | 3.1.0 | 3.1.0 | generic/mbedtls | exact | - |
| mbedtls-3.1.0 | stripped | 3.1.0 | 3.1.0 | generic/mbedtls | exact | - |
| mbedtls-3.5.2 | pristine | 3.5.2 | 3.5.2 | generic/mbedtls | exact | - |
| mbedtls-3.5.2 | stripped | 3.5.2 | 3.5.2 | generic/mbedtls | exact | - |
| mbedtls-3.6.7 | pristine | 3.6.7 | 3.6.7 | generic/mbedtls | exact | - |
| mbedtls-3.6.7 | stripped | 3.6.7 | 3.6.7 | generic/mbedtls | exact | - |
| mbedtls-4.1.1 | pristine | 4.1.1 | 4.1.1 | generic/mbedtls | exact | - |
| mbedtls-4.1.1 | stripped | 4.1.1 | 4.1.1~4.2.0 | generic/mbedtls | range | - |
| fatfs-0.10c | pristine | 0.10c | 0.10c | generic/fatfs | exact | - |
| fatfs-0.10c | touched | 0.10c | 0.10c | generic/fatfs | exact | - |
| fatfs-0.12c | pristine | 0.12c | 0.12c | generic/fatfs | exact | - |
| fatfs-0.12c | touched | 0.12c | 0.12c | generic/fatfs | exact | - |
| fatfs-0.13c | pristine | 0.13c | 0.13c | generic/fatfs | exact | - |
| fatfs-0.13c | touched | 0.13c | 0.13c | generic/fatfs | exact | - |
| fatfs-0.14b | pristine | 0.14b | 0.14b | generic/fatfs | exact | - |
| fatfs-0.14b | touched | 0.14b | 0.14b | generic/fatfs | exact | - |
| fatfs-0.15a | pristine | 0.15a | 0.15a | generic/fatfs | exact | - |
| fatfs-0.15a | touched | 0.15a | 0.15a | generic/fatfs | exact | - |
| fatfs-0.16 | pristine | 0.16 | 0.16 | generic/fatfs | exact | - |
| fatfs-0.16 | touched | 0.16 | 0.16 | generic/fatfs | exact | - |
| littlefs-2.0.5 | pristine | 2.0.5 | 2.0.5 | generic/littlefs | exact | - |
| littlefs-2.0.5 | touched | 2.0.5 | 2.0.5 | generic/littlefs | exact | - |
| littlefs-2.5.0 | pristine | 2.5.0 | 2.5.0 | generic/littlefs | exact | - |
| littlefs-2.5.0 | touched | 2.5.0 | 2.5.0 | generic/littlefs | exact | - |
| lvgl-7.11.0 | pristine | 7.11.0 | 7.11.0 | generic/lvgl | exact | - |
| lvgl-7.11.0 | stripped | 7.11.0 | 7.11.0 | generic/lvgl | exact | - |
| lvgl-8.4.0 | pristine | 8.4.0 | 8.4.0 | generic/lvgl | exact | declared: declared/cmsis-pack/LVGL.lvgl 8.4.0; bundled: generic/lodepng 2020-10-17; bundled: generic/unity 2.5.1~2.5.2 |
| lvgl-8.4.0 | stripped | 8.4.0 | 8.4.0 | generic/lvgl | exact | declared: declared/arduino/lvgl 8.4.0; declared: declared/cmsis-pack/LVGL.lvgl 8.4.0; bundled: generic/lodepng 2020-10-17; bundled: generic/unity 2.5.1~2.5.2 |
| lvgl-9.2.2 | pristine | 9.2.2 | 9.2.2 | generic/lvgl | exact | declared: declared/cmsis-pack/LVGL.lvgl 9.2.2; bundled: generic/lodepng 2023-04-10; bundled: generic/unity 2.6.0 |
| lvgl-9.2.2 | stripped | 9.2.2 | 9.2.1~9.2.2 | generic/lvgl | range | declared: declared/arduino/lvgl 9.2.2; declared: declared/cmsis-pack/LVGL.lvgl 9.2.2; bundled: generic/lodepng 2023-04-10; bundled: generic/unity 2.6.0 |
| lvgl-9.5.0 | pristine | 9.5.0 | 9.5.0 | generic/lvgl | exact | declared: declared/cmsis-pack/LVGL.lvgl 9.5.0; bundled: generic/lodepng 2023-04-10; bundled: generic/unity 2.6.0 |
| lvgl-9.5.0 | stripped | 9.5.0 | 9.5.0 | generic/lvgl | exact | declared: declared/arduino/lvgl 9.5.0; declared: declared/cmsis-pack/LVGL.lvgl 9.5.0; bundled: generic/lodepng 2023-04-10; bundled: generic/unity 2.6.0 |
| lvgl-9.6.0 | pristine | 9.6.0 | 9.6.0 | generic/lvgl | exact | declared: declared/arduino/lvgl 9.6.0; declared: declared/cmake/glfw 3.4; declared: declared/cmake/libjpeg-turbo 3.1.0; declared: declared/cmake/libpng 1.6.47; declared: declared/cmake/SDL2 2.30.11; declared: declared/cmake/SDL2_image 2.8.4; declared: declared/cmake/zlib 1.3.1; declared: declared/cmsis-pack/LVGL.lvgl 9.6.0; bundled: generic/lodepng 2023-04-10; bundled: generic/unity 2.6.0; declared: declared/cmake/fastgltf; declared: declared/cmake/freetype; declared: declared/cmake/lv_demos_ext; declared: declared/cmake/webp |
| lvgl-9.6.0 | stripped | 9.6.0 | 9.6.0 | generic/lvgl | exact | declared: declared/arduino/lvgl 9.6.0; declared: declared/cmake/glfw 3.4; declared: declared/cmake/libjpeg-turbo 3.1.0; declared: declared/cmake/libpng 1.6.47; declared: declared/cmake/SDL2 2.30.11; declared: declared/cmake/SDL2_image 2.8.4; declared: declared/cmake/zlib 1.3.1; declared: declared/cmsis-pack/LVGL.lvgl 9.6.0; bundled: generic/lodepng 2023-04-10; bundled: generic/unity 2.6.0; declared: declared/cmake/fastgltf; declared: declared/cmake/freetype; declared: declared/cmake/lv_demos_ext; declared: declared/cmake/webp |
| libcoap-4.1.2 | pristine | 4.1.2 | 4.1.2 | generic/libcoap | exact | - |
| libcoap-4.1.2 | stripped | 4.1.2 | 4.1.2 | generic/libcoap | exact | - |
| libcoap-4.2.1 | pristine | 4.2.1 | 4.2.1 | generic/libcoap | exact | - |
| libcoap-4.2.1 | stripped | 4.2.1 | 4.2.1 | generic/libcoap | exact | - |
| libcoap-4.3.0 | pristine | 4.3.0 | 4.3.0 | generic/libcoap | exact | declared: declared/cmake/external_tinydtls |
| libcoap-4.3.0 | stripped | 4.3.0 | 4.3.0 | generic/libcoap | exact | declared: declared/cmake/external_tinydtls |
| libcoap-4.3.5 | pristine | 4.3.5 | 4.3.5 | generic/libcoap | exact | declared: declared/cmake/external_tinydtls |
| libcoap-4.3.5 | stripped | 4.3.5 | 4.3.5 | generic/libcoap | exact | declared: declared/cmake/external_tinydtls |
| tinycrypt-0.2.5 | pristine | 0.2.5 | 0.2.5 | generic/tinycrypt | exact | - |
| tinycrypt-0.2.7 | pristine | 0.2.7 | 0.2.7 | generic/tinycrypt | exact | - |
| mbedtls-2.28.10 | pristine | 2.28.10 | 2.28.10 | generic/mbedtls | exact | - |
| mbedtls-2.28.10 | stripped | 2.28.10 | 2.28.10 | generic/mbedtls | exact | - |
| mbedtls-3.6.4 | pristine | 3.6.4 | 3.6.4 | generic/mbedtls | exact | - |
| mbedtls-3.6.4 | stripped | 3.6.4 | 3.6.4 | generic/mbedtls | exact | - |
| littlefs-2.9.1 | pristine | 2.9.1 | 2.9.1 | generic/littlefs | exact | - |
| littlefs-2.11.3 | pristine | 2.11.3 | 2.11.3 | generic/littlefs | exact | - |
| tinycrypt-0.2.8 | pristine | 0.2.8 | 0.2.8 | generic/tinycrypt | exact | - |
| lwip-2.2.0 | pristine | 2.2.0 | 2.2.0 | generic/lwip | exact | - |
| lwip-2.1.3 | pristine | 2.1.3 | 2.1.3 | generic/lwip | exact | - |
| libcoap-4.3.4 | pristine | 4.3.4 | 4.3.4 | generic/libcoap | exact | declared: declared/cmake/external_tinydtls |
| libcoap-4.3.4 | stripped | 4.3.4 | 4.3.4 | generic/libcoap | exact | declared: declared/cmake/external_tinydtls |
| lvgl-8.3.11 | pristine | 8.3.11 | 8.3.11 | generic/lvgl | exact | declared: declared/cmsis-pack/LVGL.lvgl 8.3.11; bundled: generic/lodepng 2020-10-17; bundled: generic/unity 2.5.1~2.5.2 |
| lvgl-8.3.11 | stripped | 8.3.11 | 8.3.11 | generic/lvgl | exact | declared: declared/arduino/lvgl 8.3.11; declared: declared/cmsis-pack/LVGL.lvgl 8.3.11; bundled: generic/lodepng 2020-10-17; bundled: generic/unity 2.5.1~2.5.2 |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos/components/thirdparty/elmfat/src | 0.13c | 0.13c | generic/fatfs | exact | bundled: generic/lodepng 2020-10-17; bundled: generic/unity 2.5.1~2.5.2; bundled: generic/freertos-kernel 10.4.0~10.4.3 |
| sdk-allwinner-r128s2-sdk-09 | lichee/dsp/kernel/FreeRTOS_xtensa_v1.7/FreeRTOS | not stated | 10.2.0~10.2.1 | generic/freertos-kernel | identified | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos/kernel/FreeRTOS-orig/Source | 10.4.3 | - | - | missing | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos/kernel/FreeRTOS/Source | 10.2.0 | - | - | missing | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/freetype | 2.13.0 | 2.13.0 | generic/freetype | exact | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/giflib/giflib-5.2.1 | 5.2.1 | 5.2.1 | generic/giflib | exact | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/libjpeg-turbo/source | 2.1.5.1 | 2.1.5~2.1.5.1 | generic/libjpeg-turbo | range | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos/components/thirdparty/lfs/littlefs-2.2.1 | 2.2 | 2.2.1 | generic/littlefs | exact | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/littlevgl-8/lvgl | 8.1.0 | 8.1.0 | generic/lvgl | exact | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/network/mbedtls-2.16.0 | 2.16.0 | 2.16.0 | generic/mbedtls | exact | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/network/mbedtls-2.7.0 | 2.7.0 | 2.7.0 | generic/mbedtls | exact | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/opus | not stated | 1.3.1 | generic/opus | identified | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/bluetooth/zephyr/src/tinycrypt | not stated | 0.2.8 | generic/tinycrypt | identified | - |
| sdk-allwinner-r128s2-sdk-09 | lichee/rtos-components/thirdparty/tinycrypt | not stated | 0.2.8 | generic/tinycrypt | identified | - |
| sdk-d1s-melis | ekernel/components/thirdparty/dfs/filesystems/elmfat | 0.12b | 0.12b | generic/fatfs | exact | - |
| sdk-d1s-melis | ekernel/components/thirdparty/dfs/filesystems/littlefs | 2.1 | 2.1.3 | generic/littlefs | exact | - |
| sdk-d1s-melis | ekernel/components/thirdparty/net/rt-thread/lwip/src/apps/mbedtls | 2.7.0 | 2.7.0 | generic/mbedtls | exact | - |
| sdk-esp8266_rtos_sdk | components/fatfs/src | 0.13c | 0.13c | generic/fatfs | exact | - |
| sdk-esp8266_rtos_sdk | components/freertos/freertos | 10.0.1 | 10.0.0~10.0.1 | generic/freertos-kernel | range | - |
| sdk-bl_iot_sdk | components/3rdparty/aws-iot/aws-iot-device-sdk-embedded-C | 3.0.1 | 3.0.1 | generic/aws-iot-device-sdk-c | exact | bundled: generic/jsmn 1.0.0 |
| sdk-bl_iot_sdk | components/os/freertos_e907 | 10.4.1 | 10.4.1 | generic/freertos-kernel | exact | - |
| sdk-bl_iot_sdk | components/platform/soc/bl602/freertos_riscv | 10.2.0 | 10.2.0 | generic/freertos-kernel | exact | - |
| sdk-bl_iot_sdk | components/platform/soc/bl602/freertos_riscv_ram | 10.2.0 | 10.2.0 | generic/freertos-kernel | exact | - |
| sdk-bl_iot_sdk | components/platform/soc/bl702/bl702_freertos | 10.2.0 | 10.2.0 | generic/freertos-kernel | exact | - |
| sdk-bl_iot_sdk | components/platform/soc/bl808/bl808_c906_freertos/Source | 10.2.1 | 10.2.1 | generic/freertos-kernel | exact | - |
| sdk-bl_iot_sdk | components/network/thread/openthread/third_party/mbedtls/repo | 2.28.0 | 2.28.0 | generic/mbedtls | exact | - |
| sdk-bl_iot_sdk | components/security/mbedtls_lts/mbedtls | 2.28.1 | 2.28.1 | generic/mbedtls | exact | - |
| sdk-bl_iot_sdk | components/network/thread/openthread | not stated | 20221027 | generic/openthread | identified | - |
| sdk-bl_iot_sdk | components/network/ble/blestack/src/common/tinycrypt | 0.2.7 | 0.2.8 | generic/tinycrypt | wrong | - |
| sdk-bouffalo_sdk | components/fs/fatfs | 0.15 | 0.15 | generic/fatfs | exact | - |
| sdk-bouffalo_sdk | components/os/freertos | 10.6.2 | 10.6.2 | generic/freertos-kernel | exact | - |
| sdk-bouffalo_sdk | components/fs/littlefs/littlefs | 2.11 | 2.11.3 | generic/littlefs | exact | - |
| sdk-bouffalo_sdk | components/crypto/mbedtls/mbedtls | 2.28.2 | 2.28.2 | generic/mbedtls | exact | - |
| sdk-bouffalo_sdk | components/crypto/mbedtls/mbedtls_v3 | 3.6.5 | 3.6.5 | generic/mbedtls | exact | - |
| sdk-bouffalo_sdk | components/ipc/open-amp/open-amp | not stated | 2025.10.0 | generic/open-amp | identified | - |
| sdk-bouffalo_sdk | components/wireless/bluetooth/blestack/src/common/tinycrypt | 0.2.7 | 0.2.8 | generic/tinycrypt | wrong | - |
| sdk-ch32v20x | EVT/EXAM/FreeRTOS/FreeRTOS_Core/FreeRTOS | 10.4.6 | 10.4.6 | generic/freertos-kernel | exact | - |
| sdk-ch32v20x | EVT/EXAM/HarmonyOS/LiteOS_m/LiteOS/kernel | not stated | 3.0~3.0.3 | generic/liteos-m-kernel | identified | - |
| sdk-ch32v20x | EVT/EXAM/RT-Thread/rt-thread/rtthread | 3.1.3 | 3.1.3 | generic/rt-thread-kernel | exact | - |
| sdk-ch32v20x | EVT/EXAM/TencentOS/TencentOS/TencentOS_Tiny/kernel/core | 2.4.5 | 2.4.5 | generic/tencentos-tiny-kernel | exact | - |
| sdk-ch32v307 | EVT/EXAM/SDIO/SDIO_SD_FATFS/FATFS | 0.14b | 0.14b | generic/fatfs | exact | - |
| sdk-ch32v307 | EVT/EXAM/FreeRTOS/FreeRTOS_Core/FreeRTOS | 10.4.6 | 10.4.6 | generic/freertos-kernel | exact | - |
| sdk-ch32v307 | EVT/EXAM/HarmonyOS/LiteOS_m/LiteOS/kernel | not stated | 3.0~3.0.3 | generic/liteos-m-kernel | identified | - |
| sdk-ch32v307 | EVT/EXAM/RT-Thread/rt-thread/rtthread | 3.1.3 | 3.1.3 | generic/rt-thread-kernel | exact | - |
| sdk-ch32v307 | EVT/EXAM/TencentOS/TencentOS/TencentOS_Tiny/kernel/core | 2.4.5 | 2.4.5 | generic/tencentos-tiny-kernel | exact | - |
| sdk-ch583 | EVT/EXAM/FreeRTOS/FreeRTOS | 10.5.1 | 10.5.1 | generic/freertos-kernel | exact | - |
| sdk-ch583 | EVT/EXAM/HarmonyOS/kernel_liteos_m/kernel | 3.2.3 | 3.2~3.2.4 | generic/liteos-m-kernel | range | - |
| sdk-ch583 | EVT/EXAM/RT-Thread/rt-thread | 3.1.5 | 3.1.5 | generic/rt-thread-kernel | exact | - |
| sdk-wm_iot_sdk | components/fatfs/src | 0.15 | 0.15 | generic/fatfs | exact | declared: declared/arduino/lvgl 8.4.0; bundled: generic/lodepng 2020-10-17; bundled: generic/unity 2.5.1~2.5.2; bundled: generic/llhttp; declared: declared/cmake/external_tinydtls |
| sdk-wm_iot_sdk | components/freertos/src | 10.4.1 | 10.4.0~10.4.1 | generic/freertos-kernel | range | - |
| sdk-wm_iot_sdk | components/coap/libcoap | 4.3.4 | 4.3.4 | generic/libcoap | exact | - |
| sdk-wm_iot_sdk | components/websockets/libwebsockets | 4.3.3 | 4.3.3 | generic/libwebsockets | exact | - |
| sdk-wm_iot_sdk | components/littlefs/src | 2.10 | 2.10.2 | generic/littlefs | exact | - |
| sdk-wm_iot_sdk | components/lvgl/lvgl | 8.4.0 | 8.4.0 | generic/lvgl | exact | - |
| sdk-wm_iot_sdk | components/mbedtls/src | 3.4.0 | 3.4.0 | generic/mbedtls | exact | - |
| sdk-wm_iot_sdk | components/wm_httpclient/http2/nghttp2 | 1.59.0 | 1.59.0 | generic/nghttp2 | exact | - |
| sdk-wm_iot_sdk | components/mqtt/paho.mqtt.c | 1.3.11 | 1.3.11 | generic/paho-mqtt-c | exact | - |

**exact** 227, **range** 23, **identified** 8, **wrong** 3, **missing** 2, **skipped** 0, **false positive** 0

Other findings: bundled 65, declared 48, duplicate 0, unexpected 0. Of 326 components reported (graded ones and every other code or binary finding), 0 are false positives.
