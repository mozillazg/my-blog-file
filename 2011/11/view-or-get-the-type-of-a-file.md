Python 内置模块 **mimetypes** 可以实现简单的基于 MIME 类型猜测文件类型的功能。

用法示例：

    >>> import mimetypes
    >>> mimetypes.guess_type('D:\Temp\hello.py')
    ('text/x-python', None)
    >>> mimetypes.guess_type('D:\Temp\6d81800ad4af5450b1351d82.jpg')
    ('image/jpeg', None)

更详细的功能见：[mimetypes — Map filenames to MIME types](http://docs.python.org/library/mimetypes.html)

