OpenWrt 21.02 i386_pentium4 repository for vlmcsd
========

Binaries built from this repository on 2023-08-23 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_21.02/i386_pentium4/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
