python-rss-download-images-script

使用的第三方库如下：

1. [Universal Feed Parser](http://www.feedparser.org)
1. [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

<span style="color:red; font-weight: blod;">参考</span>：

1. <http://code.activestate.com/recipes/577385-image-downloader/>
1. <http://www.feedparser.org/docs/>
1. <http://www.crummy.com/software/BeautifulSoup/documentation.html>
1. Python v2.6.6 documentation

这个程序有点邪恶，它的功能是解析 rss 并下载 rss 条目中的图片。目前是解析 <http://er0.tumblr.com/rss> ，这个邪恶的 rss .

代码如下:
<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import feedparser  # 解析 Feed 的库 <http://www.feedparser.org/>
from BeautifulSoup import BeautifulSoup # 解析 html xml 的库 <http://www.crummy.com/software/BeautifulSoup/>
import urllib2
from os.path import basename
from urlparse import urlsplit
import os

try:
    feed_ = feedparser.parse("http://er0.tumblr.com/rss") # 解析 rss 地址
    count = len(feed_['entries'])  # 计算条目数
    counts = [i for i in range(count)]
    descriptions = [feed_.entries[x].description for x in counts] # 获取所有条目的 description 列表
except:
    print 'RSS Error! please check!'
    exit() # 结束程序

description_soup = BeautifulSoup(''.join(descriptions))
img_src = [description_soup.findAll('img')[x]['src'] for x in counts] # 获取 descriptions 列表中的 img 标签的 src 的值

save_path = 'imgs' # 图片保存路径 
if not os.path.exists(save_path):  # 如果路径不存在
    os.makedirs(save_path) # 创建用来保存图片的文件夹

# 下载图片
for imgUrl in img_src:
    print "Start downloading", imgUrl
    try:
        imgData = urllib2.urlopen(imgUrl).read()
        fileName = save_path + '\\' + basename(urlsplit(imgUrl)[2]) # 获取图片名称
        if os.path.exists(fileName): # 如果文件名已存在
            continue
        output = open(fileName,'wb')
        output.write(imgData)
        output.close()
        print "Finished download", imgUrl
    except:
        print "Download %s failed" %imgUrl

</pre>

还需要考虑各种错误及异常，留待日后再改进。

后续将会有配置文件版及日志记录版放出
