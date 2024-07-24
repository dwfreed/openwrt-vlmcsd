OpenWrt 22.03 powerpc_464fp repository for vlmcsd
========

Binaries built from this repository on 2024-07-24 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_22.03/powerpc_464fp/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
