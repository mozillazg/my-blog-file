<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import feedparser
from BeautifulSoup import BeautifulSoup
from pprint import pprint
import urllib2
from os.path import basename
from urlparse import urlsplit
import os
import logging  # 日志相关的模块
from time import localtime, strftime

def now_time():
    return strftime('%Y/%m/%d %H:%M:%S', localtime())

log_fileName = 'log.log'   # 日志文件
    
logging.basicConfig(level=logging.INFO, filename=log_fileName)
logging.info(now_time() + ': Starting program') # 添加日志信息

logging.info(now_time() + ': Trying to read rss')
try:
    feed_ = feedparser.parse("http://er0.tumblr.com/rss")
    count = len(feed_['entries'])
    counts = [i for i in range(count)]
    descriptions = [feed_.entries[x].description for x in counts]
    description_soup = BeautifulSoup(''.join(descriptions))
    img_src = [description_soup.findAll('img')[x]['src'] for x in counts]
except:
    print 'RSS 源有问题，请检查！'
    logging.info(now_time() + ': rss error!\n')
    exit()

save_path = 'imgs'
if not os.path.exists(save_path):
    os.makedirs(save_path)

logging.info(now_time() + ': Starting download images')
for imgUrl in img_src:
    print "Starting download ", imgUrl
    logging.info(now_time() + ': Starting download ' + imgUrl)
    try:
        imgData = urllib2.urlopen(imgUrl).read()
        fileName = save_path + '\\' + basename(urlsplit(imgUrl)[2])
        if os.path.exists(fileName):
            continue
        output = open(fileName,'wb')
        output.write(imgData)
        output.close()
        print "Finished download ", imgUrl
        logging.info(now_time() + ': Finished download ' + imgUrl)
    except:
        print "Download %s failed" %imgUrl
        logging.info(now_time() + ': Download ' + imgUrl + ' failed')
        # pass
logging.info(now_time() + ': End program\n')

</pre>

更多关于日志的问题，请参考 python 帮助文档(logging)及搜索引擎