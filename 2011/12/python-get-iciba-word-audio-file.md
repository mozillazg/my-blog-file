# 从爱词霸下载单词读音音频文件

## 主要功能

 * 输入单词下载读音文件
 * 文件保存到单词开头字母的目录下
 * 可选英音或美音，默认为美音

## 系统环境

 * Windows 7 Ultimate 32-bit
 * Python 2.6.6 + BeautifulSoup 模块

## 代码

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    """从爱词霸下载单词读音音频文件
    """

    import urllib2
    import re
    import os
    from BeautifulSoup import BeautifulSoup, SoupStrainer

    def get(word, headers=None, lang='US'):
        """获取音频文件链接
        >>> get('receipt')
        http://res.iciba.com/resource/amp3/1/0/1e/11/1e11b989ba2f5e161cdad604bf3de90b.mp3
        """
        # 设置 header
        user_agent = ('Mozilla/5.0 (Windows NT 6.1; rv:9.0) '
                      + 'Gecko/20100101 Firefox/9.0')
        if headers is None:
            headers = {'User-Agent' : user_agent}
        url ='http://www.iciba.com/%s/' % urllib2.quote(word)
        # 读取网页内容
        request = urllib2.Request(url=url, headers=headers)
        try:
            html = urllib2.urlopen(request).read()
        except:
            print u'网络故障！'
            return None
        else:
            # 获取发音所在链接标签
            links = SoupStrainer('a', title=re.compile(ur'真人发音|电脑合成语音'))
            if links:
                audios = [str(tag) for tag in BeautifulSoup(html, parseOnlyThese=links)]
                soup = BeautifulSoup(''.join(audios))
                audios = soup.findAll('a')
                # print audios
                if 'US' in lang.upper() and len(audios) > 1: # 'US'
                    audio = audios[1]['onclick'].split("'")[1]
                else: # 'UK'
                    audio = audios[0]['onclick'].split("'")[1]
                return audio
            else:
                return None

    def save(url, word, headers=None, savedir=''):
        """保存音频文件
        """
        if url is None:
            print u'无音频文件可下载！'
        else:
            # 设置 header
            user_agent = ('Mozilla/5.0 (Windows NT 6.1; rv:9.0) '
                          + 'Gecko/20100101 Firefox/9.0')
            if headers is None:
                headers = {'User-Agent' : user_agent}
            headers['referer'] = 'http://www.iciba.com/%s/' % urllib2.quote(word)
            # 读取网页内容
            request = urllib2.Request(url=url, headers=headers)
            try:
                file_data = urllib2.urlopen(request).read()
            except:
                print u'网络故障！'
            else:
                starts = 'abcdefghijklmnopqrstuvwxyz'
                if not savedir:
                    savedir = '.'
                # 将文件保存到单词开头字母的文件夹中
                for i in starts:
                    if word.startswith(i):
                        savedir = savedir + os.sep + i
                        break
                else:
                    savedir = savedir + os.sep + '0-9'
                if not os.path.exists(savedir):
                    os.makedirs(savedir)
                # 保存后的文件路径
                file_name = savedir + os.sep + word +'.mp3'
                # print file_name
                # 如果文件名已存在
                if os.path.exists(file_name):
                    print u'同名文件已存在！'
                else:
                    with open(file_name,'wb') as output:
                        # 写入数据，即保存文件
                        output.write(file_data)

    def main():
        import doctest
        import audio
        doctest.testmod(audio) # 基于文档字符串的测试
        while True:
            word = raw_input("> ").strip()
            save(get(word, lang='uk'), word, savedir='audio')

    if __name__ == '__main__':
        main()

最新版本：[get\_iciba\_word_audio/audio.py](https://github.com/mozillazg/python-mini-script)


