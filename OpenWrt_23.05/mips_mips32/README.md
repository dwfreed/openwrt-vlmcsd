OpenWrt 23.05 mips_mips32 repository for vlmcsd
========

Binaries built from this repository on 2024-09-25 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_23.05/mips_mips32/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
