# python 程序报 IOError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/data1/www/htdocs/405/webpytest/1'] 错误

前段时间使用 SAE 时，出现一个有关临时文件目录的错误。

## 错误信息

>IOError: [Errno 2] No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/data1/www/htdocs/405/webpytest/1'] 

## 原因

由于没有 SAE 的系统临时文件目录的可写权限，所以报临时目录错误。

## 解决

手动指定程序所用的具有可写权限的临时目录        

    import tempfile
    tempfile.tempdir = tempdir
    # tempfile.tempdir = sae.core.get_tmp_dir() # SAE 平台的临时目录

ps1.   sae.core.get_tmp_dir() 目录暂时不具有可写权限，会报错。

ps2. 未指定临时目录时， Python 会在以下列表中查找具有可写权限的目录：
>Python查找一个标准目录列表, 将第一个用户有权限在其中创建文件的目录来设置tempdir . 这个列表是:

>   1. 环境变量TMPDIR中的目录名.

>   1. 环境变量TEMP中的目录.

>   1. 环境变量TMP中的目录.

>   1. 平台指定的位置:

>      * 在RiscOS上, 由Wimp$ScrapDir指定目录名字.
>      * 在Windows上, 以C:$backslash$TEMP, C:$backslash$TMP, $backslash$TEMP, 和 $backslash$TMP按序查找目录.
>      * 在其他平台上, 以/tmp, /var/tmp, 和/usr/tmp按序查找目录.

>   1. 最后一个是当前工作目录.

##参考

* http://pymotwcn.readthedocs.org/en/latest/documents/tempfile.html

