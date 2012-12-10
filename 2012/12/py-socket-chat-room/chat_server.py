#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
IRC 聊天室-服务器
"""

from asyncore import dispatcher
from asynchat import async_chat
import socket
import asyncore
import time

"""asyncore 库能够让程序同时处理多个连接，
实现并发处理。
允许服务器逐个对连接的用户进行服务，通过循环读取每个用户
发送的部分信息来实现并发处理。
asynchat 用于收集并处理客户端发送过来的数据
"""

PORT = 5005
NAME = '#irc1'
names = {'127.0.0.1': '小李',
         '192.168.200.114': '小明',
         '192.168.200.115': '某人',
         '192.168.200.116': '阿飞',
         '192.168.200.110': '小慧'
         }


def strf_message(name, data, users):
    """格式化消息
    """
    now = time.strftime('%H:%M:%S')
    return '[%s] <%s> %s:%s' % (now, name, data, '\n'.join(users))


class ChatSession(async_chat):
    """处理会话，收集来自客户端的数据
    """
    def __init__(self, server, sock, addr):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\n')  # 按行处理数据
        self.data = []
        self.addr = addr
        self.names = self.server.names

        ip = self.addr[0]
        self.name = self.names.get(ip, ip).replace(':', '-')
        self.server.online_users.append(self.name)
        self.server.online_users = list(set(self.server.online_users))

        # 会话产生时发送欢迎信息
        self.push(strf_message('server', '欢迎来到 %s'
                                 % self.server.name, self.server.online_users))
        self.server.broadcast(strf_message('server', '%s 已加入'
                                 % self.name, self.server.online_users))

        print '%s has entered' % str(self.addr)

    def collect_incoming_data(self, data):
        """搜集当前会话发过来的消息
        """
        self.data.append(strf_message(self.name, data,
                                      self.server.online_users))
        print self.data[-1].decode('utf8')

    def found_terminator(self):
        """将收集的消息广播给所有用户
        """
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        """会话结束时
        """
        print '%s has left' % str(self.addr)
        async_chat.handle_close(self)
        self.server.disconnect(self)


class ChatServer(dispatcher):
    """接受连接并处理会话
    """
    def __init__(self, port, name, names):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket
        self.set_reuse_addr() # 重用绑定的端口，重启服务时不用等待系统释放该端口
        self.bind(('', port))  # 绑定
        self.listen(5)
        self.name = name  # 当前服务器名称
        self.names = names  # 所有用户列表
        self.online_users = []
        self.sessions = []

    def disconnect(self, session):
        """当某个会话结束时
        """
        print self.online_users
        try:
            self.online_users.remove(session.name)
        except:
            pass
        print self.online_users
        self.broadcast(strf_message('server', '%s 已离开' % session.name,
                                    self.online_users))
        self.sessions.remove(session)

    def broadcast(self, line):
        """对所有连接进行广播
        """
        for session in self.sessions:
            session.push(line + '\n')

    def handle_accept(self):
        """当收到一个连接时，干点什么
        """
        conn, addr = self.accept()
        # 收集当前会话
        self.sessions.append(ChatSession(self, conn, addr))

if __name__ == '__main__':
    s = ChatServer(PORT, NAME, names)
    try:
        asyncore.loop()  # 启动服务器
    except KeyboardInterrupt:
        pass