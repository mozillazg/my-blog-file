# 简单获取图片 MIME 类型及解码字符串

## 获取图片 MIME 类型

<https://github.com/mozillazg/image-mime>

### 使用

    >>> with open('test', 'rb') as f:
    ...     print get_image_mime(f.read())
    ...
    image/png
    >>>
    >>> with open('test.exe', 'rb') as f:
    ...     print get_image_mime(f.read())
    ...
    application/octet-stream

## 转换未知编码的字符串为 Unicode 字符串

<https://gist.github.com/3870483>

### 使用

    >>> decode_('\xc4\xe3')
    u'\u4f60'
    >>> decode_('\xe4\xbd\xa0')
    u'\u4f60'
    >>>

