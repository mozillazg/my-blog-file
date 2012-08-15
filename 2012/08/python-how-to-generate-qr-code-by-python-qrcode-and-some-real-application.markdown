# [python]使用 python-qrcode 模块生成二维码图片


## 模块介绍

python-qrcode 是个用来生成二维码图片的第三方模块，依赖于 PIL 模块。

* <https://github.com/lincolnloop/python-qrcode>
* <http://pypi.python.org/pypi/qrcode/>


## 为什么使用要这个模块来生成二维码

* 不依赖于 java
* 跨平台


## 使用

### 简单用法

    import qrcode
    img = qrcode.make('Some data here')

### 高级用法

    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Some data')
    qr.make(fit=True)

    img = qr.make_image()

参数含义：

* version：值为1~40的整数，控制二维码的大小（最小值是1，是个12x12的矩阵）。            如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。

* error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
  * ERROR\_CORRECT\_L：大约7%或更少的错误能被纠正。
  * ERROR\_CORRECT\_M（默认）：大约15%或更少的错误能被纠正。
  * ERROR\_CORRECT\_Q：大约25%或更少的错误能被纠正。
  * ERROR\_CORRECT\_H：大约30%或更少的错误能被纠正。

* box_size：控制二维码中每个小格子包含的像素数。
* border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）


## 实际应用

我用 python-qrcode 在 Sina App Engine 上架设了一个在线生成二维码图片的网站，用来将电脑上的链接或文字保存到手机：

* <http://pyqr.sinaapp.com/>

源代码：

* <https://github.com/mozillazg/pyqr>


## 参考

 * [QR碼 - 维基百科，自由的百科全书](http://zh.wikipedia.org/wiki/QR碼 "QR碼 - 维基百科，自由的百科全书")
 * [QR Code 官网](http://www.qrcode.com/en/index.html "")

