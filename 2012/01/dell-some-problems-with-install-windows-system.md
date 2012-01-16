dell-some-problems-with-install-windows-system


# Dell 笔记本安装 Windows 操作系统曲折史

[上回](http://mozillazg.wordpress.com/dell-nldr-is-missing/)说到我在安装 Windows 操作系统时遇到了几个问题：

* 找不到硬盘，不能安装操作系统
* 读不到 U 盘

且听我一一道来。

## 找不到硬盘

PE 下找不到硬盘，没有盘符，不能使用一键 Ghost ，XP 安装盘也找不到硬盘等等，总之就是找不到硬盘。

几经折腾，才知道原来是 Boise 中 SATA 选项的缘故，只需在开机时按 F2 将 Boise 中 SATA 选项的值由 AHCI 改为 ATA 即可。

![bois1](https://github.com/mozillazg/my-blog-file/raw/master/2012/01/bois1.jpg)

网上的说法是：

> 大多数工具盘都没有自带 AHCI 驱动，不能识别 SATA 硬盘。          
> xp 安装盘也没有自带 AHCI 驱动。

如果我想要使用 SATA 特性，该如何操作呢？

* 使用 Windows 7 安装光盘安装操作系统

 记住，一定要是那种类似于原版安装盘需要手动一步一步进行安装的光盘，不能是那种使用 Ghost 方式进行安装的工具盘或修改盘，因为 Ghost 安装盘大多都不带 AHCI 驱动。

* 使用 Ghost 方式安装 Windows 7
 1. 开机按 **F2** 设置 bois 中 **SATA** 选项为 **ATA**，按 **F10** 保存并重启
 2. Ghost 安装 Windows 7
 3. <span style="color:red; font-weight: blod;">第一次重启时</span>，按 **F2** 设置 bois 中 **SATA** 的值为 **AHCI**，按 **F10** 保存并重启
 4. 等待系统安装完成

## 读不到 U 盘

刚开始时，我本来是想用 U 盘安装 Windows 7的。哪知道，当进入到安装界面时，突然读不到 U 盘了。

后来才发现，原来是因为这款笔记本的 USB 接口都是 USB 3.0 的接口，导致在没安装驱动的情况下读不了我的 2.0 的 U 盘。所以 U 盘安装系统的可能性被排除了。

后来使用光盘安装好系统后，依然不能使用 U 盘。为什么会出现这种情况呢？还是驱动的问题。因为 Windows 7 没有自带 USB 3.0 的驱动。可以使用各类拥有更新驱动功能的软件安装 USB 3.0 的驱动。

## 参考
 * <http://zhidao.baidu.com/question/235626702.html>
 * <http://zhidao.baidu.com/question/233031613.html>

