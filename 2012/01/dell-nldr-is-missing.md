# Dell 笔记本出现 NTLDR is missing 错误

最近得到了一台 Dell 笔记本。因为预装的是 Ubuntu 操作系统，
不大方便，所以我就把整个磁盘格式化了并且重新进行了分区。

问题来了，开机出现了 <cite>NTLDR is missing</cite> 错误：

> NTLDR is missing        
> Press CTRL+ALT+DEL to restart

至于是什么原因引起的。很简单，因为没有操作系统(￣_￣|||)汗！！！

写这篇文章主要是因为第一次遇到这个错误，并且发现这个错误比较常见所以记录一下。

按网上的说法 <cite> NTLDR是Win2k/XP/2k3的系统引导程序,丢失后系统将无法引导.</cite> 至于除了重装系统外还有哪些解决方法，后面的参考资料可以参考以下。
其实这个错误引出了我在装系统中遇到的诸多问题：

* PE 下找不到硬盘（没有盘符）
* xp 安装盘也找不到硬盘
* 使用 U 盘安装 Win 7，中途读不到 U 盘

详情请听下回分解：[Dell 笔记本重装 Windows 操作系统曲折史](http://mozillazg.wordpress.com/dell-some-problems-with-install-windows-system/)

至于 NTLDR is missing 的解决办法请参考：

* [戴尔笔记本启动时提示NTLDR is missing如何解决啊？ ](http://zhidao.baidu.com/question/24321096.html)
* [戴尔笔记本电脑一开机就ntldr is missing press any key to restart?](http://bbs.zhiyin.cn/viewthread.php?tid=316310)
* [How to Restore a Dell PC to Fix a Missing NTLDR](http://www.ehow.com/how_6884277_restore-pc-fix-missing-ntldr.html)
* [NTLDR is missing](http://en.community.dell.com/support-forums/disk-drives/f/3534/t/18634910.aspx)

