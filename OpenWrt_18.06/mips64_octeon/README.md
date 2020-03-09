OpenWrt repository for vlmcsd
========
Binaries built from this repository on 2020-03-09 can be downloaded from http://dwfreed.github.io/openwrt-vlmcsd/.
To install the vlmcsd package, run
```
echo "src/gz openwrt-vlmcsd http://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_18.06/mips64_octeon/base" >> /etc/opkg.conf
opkg update
opkg install vlmcsd
```
