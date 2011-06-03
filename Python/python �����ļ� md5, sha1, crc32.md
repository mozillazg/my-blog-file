python-file-hash

python,hashlib,zlib,md5,sha1,crc32

<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入文件路径返回如下信息：
# File path:
# Size:
# Date modified:
# MD5:
# SHA1:
# CRC32:
# ----------------------------------------------------------
# Author: mozillazg
# Blog: http://mzgblog.appspot.com/
# Version: 2011/5/20

import hashlib
import zlib
import os
from time import localtime, strftime

# hash 计算 MD5 、SHA1
def hash_value(filename, filesize, maxsize, xhash):
    """提供要计算 hash 值的文件路径、文件大小、每次读取的文件块大小及
    算法的摘要对象
    返回字符串类型的 hash 值
    """
    with open(filename, 'rb') as openfile: # 打开文件，一定要是以二进制打开
        while True: 
            data = openfile.read(maxsize) # 读取文件块
            if not data: # 直到读完文件
                break
            xhash.update(data)
    return xhash.hexdigest()


# CRC32 计算 CRC32
def crc32_value(filename, filesize, maxsize):
    """提供要计算 CRC32 值的文件路径、文件大小及每次读取的文件块大小
    返回整型类型的 CRC32 值
    """
    crc = 0
    with open(filename, 'rb') as openfile:
        while True: 
            data = openfile.read(maxsize) # 读取文件块
            if not data: # 直到读完文件
                break
            crc = zlib.crc32(data, crc)
    return crc


if __name__ == '__main__':
    filepath = raw_input('请输入文件路径：').strip().decode('utf-8')
    blocksize = 1024 * 1024 # 每次读取的文件块的大小（bytes）
    size = os.path.getsize(filepath) # 文件大小
    date = strftime('%Y/%m/%d %H:%M:%S', # 文件最后修改时间
                                localtime(os.path.getmtime(filepath)))
    md5 = hash_value(filepath, size, blocksize, hashlib.md5()) # 计算 MD5 值
    sha1 = hash_value(filepath, size, blocksize, hashlib.sha1()) # 计算 SHA1 值
    crc32 = crc32_value(filepath, size, blocksize) # CRC32
    
    print 'File path: %s' % filepath
    print 'Size: %s bytes' % size
    print 'Date modified: %s' % date
    #print 'MD5: %s' % md5
    #print 'SHA1: %s' % sha1
    #print 'CRC32: %x' % (crc32 & 0xffffffff)
    # 处理结果使其中的字母大写
    print 'MD5: %s' % md5.upper()
    print 'SHA1: %s' % sha1.upper()
    print 'CRC32: %X' % (crc32 & 0xffffffff)

</pre>