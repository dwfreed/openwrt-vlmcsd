OpenWrt 22.03 mipsel_24kc_24kf repository for vlmcsd
========

Binaries built from this repository on 2023-06-29 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_22.03/mipsel_24kc_24kf/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
