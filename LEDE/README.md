OpenWrt repository for vlmcsd
========
Binaries built from this repository on 2018-08-07 can be downloaded from http://dwfreed.github.io/openwrt-vlmcsd/.
To install the vlmcsd package, run
```
echo "src/gz openwrt-vlmcsd http://dwfreed.github.io/openwrt-vlmcsd/LEDE/mipsel_mips32/base" >> /etc/opkg.conf
opkg update
opkg install vlmcsd
```
