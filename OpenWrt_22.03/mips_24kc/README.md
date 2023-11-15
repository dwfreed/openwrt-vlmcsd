OpenWrt 22.03 mips_24kc repository for vlmcsd
========

Binaries built from this repository on 2023-11-15 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_22.03/mips_24kc/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
