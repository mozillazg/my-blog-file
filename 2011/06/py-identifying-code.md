## 生成简单的包含文字的图片(验证码)

一个非常简单的验证码程序，只是生成一个包含文字的图片。

用到了 [PIL(Python Imaging Library)](http://www.pythonware.com/products/pil/) 模块。

### 注意
官方提供的 PIL 安装包在设置文字字体（TrueType 或 OpenType 字体）时会出现如下错误：

>ImportError: The _imagingft C module is not installed

### 解决
Windows 用户可以到 <http://www.lfd.uci.edu/~gohlke/pythonlibs/> 下载第三方编译的 PIL 安装包，至于非 Windows 用户请参考： <http://stackoverflow.com/questions/4011705/python-the-imagingft-c-module-is-not-installed>

###代码如下：

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    """生成简单的包含文字的图片
    """


    import Image
    import ImageDraw
    import ImageFont

    # 新建图片
    img = Image.new("RGB", (100, 60))
    # 绘制图片
    draw = ImageDraw.Draw(img)
    # 字体
    font = ImageFont.truetype('wqy-microhei.ttc', 20)
    # 绘入文字
    draw.text((10, 20), u"test 测试", font=font)
    # 保存到文件
    img.save('test.png', 'png')
    # 显示图片
    img.show()

### 生成的图片
![py-identifying-code-test-png](https://github.com/mozillazg/my-blog-file/raw/master/2011/06/test.png)
