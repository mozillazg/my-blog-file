python-rss-download-images-script-multi-thread-queue
Universal Feed Parse,BeautifulSoup,urllib2,thread,queue,python download image,gui,er0,agebo ero部

<pre class="prettyprint">

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
from os.path import basename
from urlparse import urlsplit
import os
from pprint import pprint
from threading import Thread
from Queue import Queue
import time
import sys
# Universal Feed Parser(http://www.crummy.com/software/BeautifulSoup/)
import feedparser
# BeautifulSoup(http://www.crummy.com/software/BeautifulSoup/)
from BeautifulSoup import BeautifulSoup

time1 = time.time()

try:
    # 解析 rss 地址
    feed_ = feedparser.parse("http://er0.tumblr.com/rss")
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

# 多线程

q = Queue()

def download_img(img_src, savePath):
    try:
        imgData = urllib2.urlopen(img_src).read()
        # 获取图片名称
        fileName = save_path + '\\' + basename(urlsplit(img_src)[2])
        # 文件名是否存在
        if not os.path.exists(fileName): 
            output = open(fileName,'wb+')
            output.write(imgData)
            output.close()
            print "Finished download %s\n" %img_src
    except:
        print "Download %s failed\n" %img_src

def worker():
    while True:
        download_img(q.get(), save_path)
        q.task_done()

def download_imgs(imgs_src, save_path, num_workers):
    for i in range(num_workers):
        t = Thread(target=worker)
        t.setDaemon(True)
        t.start()
    # 下载图片
    for img_src in imgs_src:
        q.put(img_src, save_path)
    q.join()

def process(imgs_src, save_path, numthreads):
    if numthreads > 1:
        download_imgs(imgs_src, save_path, numthreads)
    else:
        for img_src in imgs_src:
            try:
                imgData = urllib2.urlopen(img_src).read()
                # 获取图片名称
                fileName = save_path + '\\' + basename(urlsplit(img_src)[2])
                # 文件名是否存在
                if not os.path.exists(fileName):
                    output = open(fileName,'wb+')
                    output.write(imgData)
                    output.close()
                    print "Finished download %s\n" %img_src
            except:
                print "Download %s failed\n" %img_src

if __name__ == '__main__':
    process(imgs_src, save_path, int(sys.argv[1]))
    time2 = time.time()
    print time2 - time1
 

</pre>