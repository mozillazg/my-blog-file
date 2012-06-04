# [windows]在安全模式下启动需要的服务

## 安全模式下启动额外的服务

默认情况下，安全模式只能启动一些基本的系统服务，其他的系统服务及软件服务根本就不能启动，会报如下类似错误：

![service error](https://github.com/mozillazg/my-blog-file/raw/master/2012/04/2012-06-04_23-00-55.png "service error")

下面将要介绍的方法可以解决这个问题。

废话不多说了，直接上案例。

### 在安全模式下启动 Windows Installer 服务

#### 系统环境

 * Windows 7 Ultimate 32-bit

普通情况下，在安全模式下启动 Windows Installer 服务会出现如下错误：

![service error](https://github.com/mozillazg/my-blog-file/raw/master/2012/04/2012-06-04_23-00-55.png "service error")

![windows installer service error](https://github.com/mozillazg/my-blog-file/raw/master/2012/04/xxx.png "windows installer service error")

通过修改注册表可以实现在安全模式下启动 windows installer 服务：

**以下操作最好在安全模式下进行（方便查看哪些服务在安全模式下能启动）**

1. 打开[服务]控制台，获取 windows installer 服务的服务名称：msiserver。

 ![windows installer servce name](https://github.com/mozillazg/my-blog-file/raw/master/2012/04/2012-05-03_20-21-52.png "windows installer servce name")

2. 打开[注册表]，定位到 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\` 。

 1. 如果是[安全模式]，打开 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal` 。

 2. 如果是[网络安全模式]，打开 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Network` 。

3. 新建值为服务名称的项，本例是 msiserver 。

 ![new key name service name](https://github.com/mozillazg/my-blog-file/raw/master/2012/04/2012-05-03_20-21-15.png "new key name service name")

4. 更改该项的默认值为 Service 。

 ![change default value to Service](https://github.com/mozillazg/my-blog-file/raw/master/2012/04/2012-05-03_20-21-15.png "change default value to Service")

5. 检查 Windows Installer 服务的依存服务是否全部能够启动。如果有不能启动的，按照上面的步骤修改注册表即可。

 ![check ](https://github.com/mozillazg/my-blog-file/raw/master/2012/04/2012-05-03_20-22-18.png "")

结果：

 ![start windows installer service in safe mode](https://github.com/mozillazg/my-blog-file/raw/master/2012/04/2012-05-10_21-55-01.png "start windows installer service in safe mode")

有的服务需要相关驱动支持，比如说音频服务除了需要启动相关音频服务外还需要加载相关声卡驱动。又该如何操作呢？请听下回分解。

## 参考

 * [How To Uninstall Software In Windows Safe Mode](http://www.ghacks.net/2010/07/18/how-to-uninstall-software-in-windows-safe-mode/ "How To Uninstall Software In Windows Safe Mode")



安全模式下启动其他服务, starting services in safe mode, safe mode, uninstall software, windows installer, windows registry, windows safe mode

