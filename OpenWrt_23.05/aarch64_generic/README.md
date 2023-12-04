OpenWrt 23.05 aarch64_generic repository for vlmcsd
========

Binaries built from this repository on 2023-12-04 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_23.05/aarch64_generic/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
