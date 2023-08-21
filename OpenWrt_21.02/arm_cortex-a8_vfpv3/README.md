OpenWrt 21.02 arm_cortex-a8_vfpv3 repository for vlmcsd
========

Binaries built from this repository on 2023-08-21 can be downloaded from <https://dwfreed.github.io/openwrt-vlmcsd/>.

To install the vlmcsd package, run

```
echo "src/gz openwrt-vlmcsd https://dwfreed.github.io/openwrt-vlmcsd/OpenWrt_21.02/arm_cortex-a8_vfpv3/base" >> /etc/opkg/customfeeds.conf
opkg update
opkg install vlmcsd
```
