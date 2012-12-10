#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import socket
import thread

import wx


def expor(event):
    path = wx.FileSelector('select a file')
    if path:
        filename.SetValue(path)


def upload_file():
    with open(filename.GetValue(), 'rb') as f:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conn.connect(('127.0.0.1', 5200))
        file_content = f.read()
        contents.AppendText('start upload...\n')
        conn.send(file_content)
        contents.AppendText(conn.recv(1024) + '\n')
        conn.close()


def thread1():
    wx.CallAfter(upload_file)


def upload(event):
    thread.start_new_thread(thread1, ())

if __name__ == '__main__':

    app = wx.App()
    win = wx.Frame(None, title='Simple File Uploader', size=(410, 255))
    bkg = wx.Panel(win)

    upload_button = wx.Button(bkg, label='Upload')
    upload_button.Bind(wx.EVT_BUTTON, upload)
    filename = wx.TextCtrl(bkg)
    contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

    hbox = wx.BoxSizer()
    hbox.Add(filename, proportion=1, flag=wx.EXPAND)
    hbox.Add(upload_button, proportion=0, flag=wx.LEFT, border=5)
    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
    vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT
             | wx.BOTTOM | wx.RIGHT, border=5)
    bkg.SetSizer(vbox)

    filename.Bind(wx.EVT_LEFT_DOWN, expor)

    win.Show()
    app.MainLoop()
