python-rss-download-images-script-wxPython
Universal Feed Parse,BeautifulSoup,urllib2,wx,wxPython,python download image,gui,er0,agebo ero部

<pre class="prettyprint">
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
import os
from os.path import basename
from urlparse import urlsplit
from pprint import pprint
# 解析 Feed 的库(http://www.feedparser.org/)
import feedparser
# 解析 html xml 的库 <http://www.crummy.com/software/BeautifulSoup/>
from BeautifulSoup import BeautifulSoup
import wx   # wxPython

# 批量下载图片到指定目录
def download_imgs(imgSrc, savePath):
    # 下载图片
    for imgUrl in imgSrc:
        contents.AppendText("Start download " + imgUrl + '\n')
        try:
            imgData = urllib2.urlopen(imgUrl).read()
            # 获取图片名称
            fileName = savePath + '\\' + basename(urlsplit(imgUrl)[2])
            # 如果文件名已存在
            if os.path.exists(fileName):
                # 跳过此次循环
                continue
            output = open(fileName,'wb')
            output.write(imgData)
            output.close()
            contents.AppendText("Finished download " + imgUrl + '\n')
        except:
            contents.AppendText("Download " + imgUrl + ' failed\n')


def rss(event):
    contents.SetValue("Start program\n")
    try:
        # 解析 rss 地址
        feed_ =feedparser.parse(rsslink.GetValue())
        # 计算条目数
        count = len(feed_['entries'])
        counts = [i for i in range(count)]
        # 获取所有条目的 description 列表
        descriptions = [feed_.entries[x].description for x in counts]
        description_soup = BeautifulSoup(''.join(descriptions))
        # 获取 descriptions 列表中的 img 标签的 src 的值
        img_src = [description_soup.findAll('img')[x]['src'] for x in counts]
    except:
        contents.AppendText('RSS Error! please check!\n')
        contents.AppendText('End program\n')
    else:

        # 图片保存路径 
        save_path = imgsdir.GetValue()
        # 如果路径不存在
        if not os.path.exists(save_path):
            # 创建用来保存图片的文件夹
            os.makedirs(save_path)

        # 下载图片
        download_imgs(img_src, save_path)
        contents.AppendText('End program\n')


def dirs(event):
    dir = wx.DirDialog(bkg, 'Choose a folder to save the images', 
                        style=wx.DD_DEFAULT_STYLE)
    if dir.ShowModal() == wx.ID_OK:
        path = dir.GetPath()
        imgsdir.SetValue(path)
    dir.Destroy()

    
app = wx.App()
win = wx.Frame(None, title="Download RSS Images", size=(500, 335))
bkg = wx.Panel(win)

chooseButton = wx.Button(bkg, label='Browse...')
chooseButton.Bind(wx.EVT_BUTTON, dirs)

loadButton = wx.Button(bkg, label='Download')
loadButton.Bind(wx.EVT_BUTTON, rss)

label1 = wx.StaticText(bkg,1,"Folder: ")
label2 = wx.StaticText(bkg,1,"   RSS: ")
rsslink = wx.TextCtrl(bkg,-1,"http://er0.tumblr.com/rss")
imgsdir = wx.TextCtrl(bkg, -1, "imgs")
contents = wx.TextCtrl(bkg, style=wx.TE_READONLY | 
                            wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(label1, proportion=0, flag=wx.ALIGN_CENTRE|wx.ALL, border=5)
hbox.Add(imgsdir, 1, wx.EXPAND, 5)
hbox.Add(chooseButton, 0, wx.LEFT, 5)

ibox = wx.BoxSizer()
ibox.Add(label2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
ibox.Add(rsslink, 1, wx.EXPAND, 5)
ibox.Add(loadButton, 0, wx.LEFT, 5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, 0, wx.EXPAND | wx.ALL, 5)
vbox.Add(ibox, 0, wx.EXPAND | wx.ALL, 5)
vbox.Add(contents, proportion=1,
         flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()


</pre>