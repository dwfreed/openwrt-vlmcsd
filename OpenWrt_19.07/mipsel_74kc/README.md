OpenWrt repository for vlmcsd
========
Binaries built from this repository on 2020-03-09 can be downloaded from http://dwfreed.github.io/openwrt-vlmcsd/.
To install the vlmcsd package, run
```
echo "src/gz openwrt-vlmcsd http://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_19.07/mipsel_74kc/base" >> /etc/opkg.conf
opkg update
opkg install vlmcsd
```
