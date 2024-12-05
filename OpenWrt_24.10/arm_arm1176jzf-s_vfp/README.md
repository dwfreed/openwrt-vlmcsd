OpenWrt 24.10 arm_arm1176jzf-s_vfp repository for vlmcsd
========

Binaries built from this repository on 2024-12-05 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_24.10/arm_arm1176jzf-s_vfp/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
