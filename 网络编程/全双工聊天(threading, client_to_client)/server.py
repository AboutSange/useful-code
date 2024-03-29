#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
服务器用来中转和保存关系
"""


import socket
import sys
import threading
import re
from time import *

reload(sys)
sys.setdefaultencoding('utf-8')

HOST = '127.0.0.1'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ss.bind(ADDR)
ss.listen(5)

user_sock_dict = {}  # username --> socket，记录已连接的客户端的用户名和套接字的关系
sock_sock_dict = {}  # user1.socket --> user2.socket，记录通信双方的套接字的对应关系


def message_transform(sock, addr, user):
    """
    处理客户端确定用户名之后发送的文本
    通信文本类型：
        None
        Quit
        To:someone
        其他文本
    :param sock:
    :param addr:
    :param user:
    :return:
    """
    def _quit():
        if sock in sock_sock_dict:
            data = 'Quit.'  # Quit.
            sock_sock_dict[sock].sendall(data)
            del sock_sock_dict[sock_sock_dict[sock]]
            del sock_sock_dict[sock]
        del user_sock_dict[user]
        sock.close()
        print '已与{0}断开连接'.format(addr)

    while True:
        try:
            data = sock.recv(BUFSIZE)
        except Exception as e:
            print e
            _quit()
            break
        print '[{0}]{1} {2}: {3}'.format(ctime(), addr, user, data)
        if not data or data == 'Quit':
            sock.sendall(data)
            _quit()
            break
        elif re.match('^To:.+', data) is not None:
            data = data[3:]
            if data in user_sock_dict:
                if data == user:
                    sock.sendall('您正在与自己聊天，输入To:<someone>与someone开始聊天吧')
                else:
                    sock_sock_dict[sock] = user_sock_dict[data]
                    sock_sock_dict[user_sock_dict[data]] = sock
                    sock.sendall('您即将与 {0} 开始聊天'.format(data))
                    sock_sock_dict[sock].sendall('{0} 请求跟您聊天'.format(user))
            else:
                sock.sendall('用户 {0} 不存在'.format(data))
        else:
            if sock in sock_sock_dict:
                sock_sock_dict[sock].sendall('[{0}] {1}: {2}'.format(ctime(), user, data))
            else:
                sock.sendall('没人正在与您聊天，输入To:<someone>与someone开始聊天吧')


def connect_thread(sock, addr):
    """
    连接成功后需要输入一个用户名
    用户名类型：
        已存在
        （客户端直接输入ctrl+c退出）
        合法用户名
    :param sock: 客户端的socket
    :param addr: 客户端的addr
    :return:
    """
    # 设置用户名
    user = None
    while True:
        try:
            username = sock.recv(BUFSIZE)
        except Exception as e:
            print e
            print '客户端{0}未设置用户名，并已退出'.format(addr)
            break
        if not username:  # 客户端未输入用户名就退出
            print '客户端{0}未设置用户名，并已退出'.format(addr)
            break
        if username in user_sock_dict:
            sock.sendall('REUSE')
        else:
            sock.sendall('设置用户名成功，您的用户名为：{0}'.format(username))
            user_sock_dict[username] = sock
            user = username
            break

    if not user:
        sock.close()
        return

    print '客户端{0}的用户名为：{1}'.format(addr, user)

    message_transform(sock, addr, user)


if __name__ == '__main__':
    print '服务已启动，地址为{0}'.format(ADDR)
    while True:
        cs, addr = ss.accept()
        print '已与{0}建立连接'.format(addr)
        chat = threading.Thread(target=connect_thread, args=(cs, addr))
        chat.start()