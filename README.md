openwrt-vlmcsd

a package for vlmcsd

1. 把下面一行：

   srv-host=_vlmcs._tcp.lan,lede.lan,1688,0,100
   
   添加到 /etc/dnsmasq.conf .(其中lede.lan根据系统管理中的主机名更改，比如你主机名是lede那么此处填写lede.lan，或者直接改成LAN口IP）

2. 重启dnsmasq: 在路由器SSH中运行：

   /etc/init.d/dnsmasq restart

   然后在win命令行运行：nslookup -type=srv _vlmcs._tcp.lan  如果正确返回了路由器IP则成功，继续下一步。

3. /etc/init.d/vlmcsd enable && /etc/init.d/vlmcsd start && /etc/init.d/dnsmasq restart
   
   OK, 你的路由器下应该可以自动激活Windows或者Office了 :)

配套luci: [luci-app-vlmcsd](https://github.com/mchome/luci-app-vlmcsd ""), 可自动修改dnsmasq.conf实现自动激活，无需上述配置
