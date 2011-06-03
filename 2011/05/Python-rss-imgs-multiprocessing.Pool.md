python-rss-download-images-script-multiprocessing-pool
multiprocessing.Pool
Universal Feed Parse,BeautifulSoup,urllib2,multiprocessing,Pool,multi,process,python download image,gui,er0,agebo ero部

HOW TO USE:

e.g.: 
<pre class="prettyprint">
python download_agebo_ero_img.py 2
</pre>

<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# python download_agebo_ero_img.py 2

import urllib2
from os.path import basename
from urlparse import urlsplit
import os
import multiprocessing
import time
import sys
# Universal Feed Parser(http://www.crummy.com/software/BeautifulSoup/)
import feedparser
# BeautifulSoup(http://www.crummy.com/software/BeautifulSoup/)
from BeautifulSoup import BeautifulSoup

def download_imgs(img_src):
    try:
        imgData = urllib2.urlopen(img_src).read()
        # 获取图片名称
        fileName = save_path + '\\' + basename(urlsplit(img_src)[2])
        # 文件名是否存在
        if not os.path.exists(fileName):
            output = open(fileName,'wb')
            output.write(imgData)
            output.close()
            return "Finished download " + img_src +"\n"
    except:
        return "Download "+ img_src +" failed\n" 

def process(imgs_src, chunksize, numprocess):
    pool = multiprocessing.Pool(numprocess)
    result = pool.map_async(download_imgs, imgs_src, chunksize)
    pool.close()
    return result.get()


if __name__ == '__main__':

    time1 = time.time()
    
    try:
        # 解析 rss 地址
        feed_ = feedparser.parse("agebo_ero.xml")
        # 计算条目数
        count = len(feed_['entries'])
        counts = [i for i in range(count)]
    
        # 获取所有条目的 description 列表
        descriptions = [feed_.entries[x].description for x in counts]
        description_soup = BeautifulSoup(''.join(descriptions))
        # 获取 descriptions 列表中的 img 标签的 src 的值
        imgs_src = [description_soup.findAll('img')[x]['src'] for x in counts]
    except:
        print 'RSS Error! please check!'
        # 结束程序
        exit()
    
    # 图片保存路径 
    save_path = 'imgs'
    # 如果路径不存在
    if not os.path.exists(save_path):
        # 创建用来保存图片的文件夹
        os.makedirs(save_path)
    chunksize = 2   # 每块中的项目数
    result = process(imgs_src, chunksize, int(sys.argv[1]))
    print ''.join(result)
    time2 = time.time()
    print time2 - time1
 
</pre>