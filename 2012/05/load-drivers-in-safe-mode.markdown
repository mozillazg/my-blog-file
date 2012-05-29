# [windows]在安全模式下载入想要的驱动

[上文]( "")说了如何在安全模式下启动想要的服务。因为某些服务需要载入相关的驱动才能正常工作，所以本文说一下如何在安全模式下载入想要的驱动。

还是举个例子：如何在安全模式下启动放歌（启动音频服务+载入音频驱动）。

1. 按照前文所诉，修改相关注册表项以便能在安全模式下启动音频服务。
 1. 注意要将依赖的服务都添加进去。

 ![audio-services](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-04-14_20-05-24.png "")
 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-29-30.png "")
 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-04-14_20-05-48.png "")
 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-26-59.png "")
 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-26-11.png "")
 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-27-39.png "")
 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-28-49.png "")
2. 打开[设备管理器]，获取音频驱动的属性“设备类 GUID”及“类短名称”的值。

 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-42-39.png "")
 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-40-05.png "")
 ![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-40-15.png "")
3. 使用上面的值修改注册表：

![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-05-29_22-43-34.png "")
4. 重启系统。

![](https://github.com/mozillazg/my-blog-file/raw/master/2012/05/2012-04-14_20-34-27.png "")

