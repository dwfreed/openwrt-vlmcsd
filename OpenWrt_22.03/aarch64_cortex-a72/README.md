OpenWrt 22.03 aarch64_cortex-a72 repository for vlmcsd
========

Binaries built from this repository on 2023-11-16 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_22.03/aarch64_cortex-a72/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
