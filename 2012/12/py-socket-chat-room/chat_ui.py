#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
IRC 聊天室-客户端
"""

import socket
import threading
from xml.sax.saxutils import escape
import wx
import wx.lib.buttons as buttons
import wx.html

# 定义一个全局变量用于判断是否已连接服务器
is_connected = False

# 定义一个 wxPython 事件 ID
EVT_RESULT_ID = wx.NewId()


def EVT_RESULT(win, func):
    """定义一个事件类型"""
    win.Connect(-1, -1, EVT_RESULT_ID, func)


class ResultEvent(wx.PyEvent):
    """初始化事件类型"""
    def __init__(self, data):
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data


# 用于获取消息的线程
class WorkerThread(threading.Thread):
    """用于获取服务器消息的线程"""
    def __init__(self, s, notify_window, change_status):
        threading.Thread.__init__(self)
        self.s = s
        self.unactived_status = change_status
        self._notify_window = notify_window

        self.start()

    def run(self):
        global is_connected
        while True:
            # print 'thread', is_connected
            if not is_connected:
                break
                # continue
            try:
                data = self.s.recv(1024)
            except socket.error:
                # pass
                try:
                    # self.unactived_status()
                    self.chat_contents.AppendToPage(u'<p>与服务器失去连接</p>')
                except:
                    pass
                is_connected = False
            else:
                try:
                    wx.PostEvent(self._notify_window, ResultEvent(data + '\n'))
                except:
                    pass


# main frame
class MainFrame(wx.Frame):
    def __init__(self, parent, id, size=(700, 500)):
        wx.Frame.__init__(self, parent, id, u'SIRC（一个简单的 IRC 聊天室）',
                          size=size)
        # 设置窗口最小尺寸
        self.SetMinSize(size)

        # 显示窗口图标及托盘图标（伪）
        icon_big = wx.Icon('images/irc_big.ico', wx.BITMAP_TYPE_ICO)
        icon_small = wx.Icon('images/irc_small.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon_small)
        self.taskicon = wx.TaskBarIcon()
        self.taskicon.SetIcon(icon_big)

        bkg = wx.Panel(self, -1)

        # 左边
        self.user_lists = wx.TextCtrl(bkg, 0, u'昵称\n\n', style=wx.TE_READONLY
                                      | wx.TE_MULTILINE, size=(150, -1))
        self.start_button = wx.Button(bkg, 0, u'连接', size=(50, 30))
        self.stop_button = wx.Button(bkg, 0, u'断开', size=(50, 30))
        self.start_button.Bind(wx.EVT_BUTTON, self.start_conn)
        self.stop_button.Bind(wx.EVT_BUTTON, self.stop_conn)

        # 右边
        self.chat_contents = wx.html.HtmlWindow(bkg, 0, style=wx.TE_MULTILINE
                                                | wx.TE_READONLY,
                                                size=(380, -1))
        self.chat_contents.SetBorders(1)
        self.input_area = wx.TextCtrl(bkg, 0, '', size=(100, 30))
        self.send_button = wx.Button(bkg, 0, u'发送', size=(50, 30))
        self.send_button.Bind(wx.EVT_BUTTON, self.send_message)

        # 布局
        hbox0 = wx.BoxSizer()
        hbox0.Add(self.start_button, proportion=4, flag=wx.EXPAND | wx.ALL,
                  border=0)
        hbox0.Add(self.stop_button, proportion=4, flag=wx.EXPAND | wx.ALL,
                  border=0)

        vbox0 = wx.BoxSizer(wx.VERTICAL)
        vbox0.Add(self.user_lists, proportion=6, flag=wx.EXPAND | wx.ALL,
                  border=5)
        vbox0.Add(hbox0, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        hbox2 = wx.BoxSizer()

        # 表情
        self.smileys = {':-) ': 'images/Smiley_Smile.ico',
                        ':-)) ': 'images/Smiley_Happy.ico',
                        ':-( ': 'images/Smiley_Sad.ico'
                        }
        for tip, path in self.smileys.items():
            smiley = wx.Image(path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            button = buttons.GenBitmapTextButton(bkg, -1, smiley,
                                                 size=(30, 30))
            button.SetUseFocusIndicator(False)
            button.SetToolTipString(tip)
            button.Bind(wx.EVT_BUTTON, self.smiley)
            hbox2.Add(button, proportion=0, flag=wx.ALIGN_CENTER)

        hbox2.Add(self.input_area, proportion=5, flag=wx.LEFT, border=5)
        hbox2.Add(self.send_button, proportion=0, border=5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.chat_contents, proportion=6, flag=wx.EXPAND
                 | wx.ALL | wx.TE_MULTILINE, border=5)
        vbox.Add(hbox2, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        hbox = wx.BoxSizer()
        hbox.Add(vbox0, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        hbox.Add(vbox, proportion=8, flag=wx.EXPAND | wx.ALL, border=5)

        bkg.SetSizer(hbox)

        # 绑定后台事件
        EVT_RESULT(self, self.read_message)

        # 关闭程序时，干点其他的清理工作
        self.Bind(wx.EVT_CLOSE, self.close_)

        self.stop_button.Enable(False)
        self.pre_message = None

        self.host = '192.168.200.116'
        self.port = 5005

    def start_conn(self, event):
        """按下连接按钮时，进行相关操作
        """
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.s.connect((self.host, self.port))
        except socket.error:
            self.unactived_status()
            self.chat_contents.AppendToPage(u'<p>无法连接服务器</p>')
        global is_connected

        is_connected = True
        # 启动接受消息的线程
        WorkerThread(self.s, self, self.unactived_status)

        # 改变按钮状态
        self.start_button.Enable(False)
        self.stop_button.Enable(True)

    def stop_conn(self, event):
        """按下断开按钮时，进行相关操作
        """
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()
        # del self.s
        global is_connected
        is_connected = False
        self.unactived_status()

    def smiley(self, event):
        """按下表情按钮时，进行相关操作
        """
        button = event.GetEventObject()
        value = button.GetToolTipString()
        self.input_area.AppendText(value)

    def send_message(self, event):
        """按下发送按钮时，执行相关操作
        """
        message = self.input_area.GetValue()
        if message:
            try:
                self.s.send(message.encode('utf8') + '\n')
                self.input_area.SetValue('')
                print message
            except AttributeError:
                self.chat_contents.AppendToPage(u'<p>请先连接服务器</p>')
            except socket.error:
                self.unactived_status()
                self.chat_contents.AppendToPage(u'<p>请先连接服务器</p>')
        else:
            self.chat_contents.AppendToPage(u'<p>内容不能为空</p>')

    def read_message(self, event):
        """处理接收的消息
        """
        if event.data.strip():
            data = event.data
            if data == self.pre_message:
                return
            self.pre_message = data
            data = data.decode('utf8')
            flag_index = data.rfind(':')
            if flag_index == -1:
                return
            users = ''.join([i for i in data[flag_index + 1:]])
            self.user_lists.SetValue(users)

            messages = data[:flag_index]
            if not messages:
                return
            print repr(messages)
            messages = u'<p>%s</p>' % escape(messages)
            for tip, path in self.smileys.items():
                messages = messages.replace(tip, u'<img src="%s" title="%s">'
                                            % (path, tip))
            self.chat_contents.AppendToPage(messages)

    def unactived_status(self):
        """
        """
        self.chat_contents.SetPage(u'')
        self.user_lists.SetValue(u'')
        self.stop_button.Enable(False)
        self.start_button.Enable(True)

    def close_(self, event):
        """关闭时执行一些操作
        """
        try:
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            self.chat_contents.close()
        except:
            pass
        global is_connected
        is_connected = False
        print 'closing'

        # 调用 Skip() 执行默认的关闭操作
        event.Skip()
        self.Destroy()
        exit(0)


class MainApp(wx.App):
    def OnInit(self):
        """重载 OnInit 方法
        """
        self.frame = MainFrame(None, -1)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()