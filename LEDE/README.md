OpenWrt repository for vlmcsd
========
Binaries built from this repository on 2018-06-08 can be downloaded from http://cokebar.github.io/openwrt-vlmcsd/.
To install the vlmcsd package, run
```
echo "src/gz announce http://cokebar.github.io/openwrt-vlmcsd/LEDE" >> /etc/opkg.conf
opkg update
opkg install vlmcsd
```
