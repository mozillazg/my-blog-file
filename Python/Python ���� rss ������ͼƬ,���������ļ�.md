
python-rss-download-images-script
Universal Feed Parse,BeautifulSoup,urllib2,python download image,er0,agebo ero部

<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import feedparser # 解析 Feed 的库 <http://www.feedparser.org/>
from BeautifulSoup import BeautifulSoup # 解析 html xml 的库 <http://www.crummy.com/software/BeautifulSoup/>
import urllib2
from os.path import basename
from urlparse import urlsplit
import os
import ConfigParser # 与配置文件相关的模块

CONFIGFILE = 'config.py' # 配置文件名称

config = ConfigParser.RawConfigParser()
config_cheek= False
try:
    config.read(CONFIGFILE)
except:
    config_cheek = True
if config_cheek or len(config.read(CONFIGFILE)) == 0: # 如果配置文件有问题，生成包含默认配置的配置文件
    config.add_section('General')
    config.set('General', 'feed', 'http://er0.tumblr.com/rss')
    config.set('General', 'save_path', 'imgs')
    with open(CONFIGFILE, 'wb') as configfile:
        config.write(configfile)
    config.read(CONFIGFILE)
    
# 如果配置项 feed 不存在，添加它
try:
    rss = config.get('General', 'feed')
except:
        config.add_section('General')
        config.set('General', 'feed', 'http://er0.tumblr.com/rss')
        with open(CONFIGFILE, 'wb') as configfile:
            config.write(configfile)
        config.read(CONFIGFILE)
        rss = config.get('General', 'feed')

try:
    feed_ = feedparser.parse(rss) # 解析 rss 地址
    count = len(feed_['entries']) # 计算条目数
    counts = [i for i in range(count)]
    descriptions = [feed_.entries[x].description for x in counts] # 获取所有条目的 description 列表

    description_soup = BeautifulSoup(''.join(descriptions))
    img_src = [description_soup.findAll('img')[x]['src'] for x in counts] # 获取 descriptions 列表中的 img 标签的 src 的值
except:
    print 'RSS Error! please check!'
    exit() # 结束程序
    
# 如果配置项 save_path 不存在，添加它
try:
    save_path = config.get('General', 'save_path')
except:
    config.set('General', 'save_path', 'imgs')
    with open(CONFIGFILE, 'wb') as configfile:
        config.write(configfile)
    config.read(CONFIGFILE)
    save_path = config.get('General', 'save_path')
if not os.path.exists(save_path):
    os.makedirs(save_path)


for imgUrl in img_src:
    print "Start downloading", imgUrl
    try:
        imgData = urllib2.urlopen(imgUrl).read()
        fileName = save_path + '\\' + basename(urlsplit(imgUrl)[2])
        if os.path.exists(fileName):
            continue
        output = open(fileName,'wb')
        output.write(imgData)
        output.close()
        print "Finished download", imgUrl
    except:
        print "Download %s failed" %imgUrl

</pre>

更多关于配置的问题，请参考 python 帮助文档(ConfigParser)或 baidu/google 关键字 ptyhon ConfigParser
