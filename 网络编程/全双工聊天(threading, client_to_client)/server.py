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

clients = {}  # username --> socket，记录已连接的客户端的用户名和套接字的关系
chatwith = {}  # user1.socket --> user2.socket，记录通信双方的套接字的对应关系


def message_transform(sock, user):
    """
    处理客户端确定用户名之后发送的文本
    通信文本类型：
        None
        Quit
        To:someone
        其他文本
    :param sock:
    :param user:
    :return:
    """
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            if sock in chatwith:
                chatwith[sock].sendall(data)
                del chatwith[chatwith[sock]]
                del chatwith[sock]
            del clients[user]
            sock.close()
            break
        if data == 'Quit':
            sock.sendall(data)
            if sock in chatwith:
                data = '{0}.'.format(data)
                chatwith[sock].send(data)
                del chatwith[chatwith[sock]]
                del chatwith[sock]
            del clients[user]
            sock.close()
            break
        elif re.match('^To:.+', data) is not None:
            data = data[3:]
            if data in clients:
                if data == user:
                    sock.send('Please don\'t try to talk with yourself.')
                else:
                    chatwith[sock] = clients[data]
                    chatwith[clients[data]] = sock
            else:
                sock.send('the user %s is not exist' % data)
        else:
            if sock in chatwith:
                chatwith[sock].send('[%s] %s: (%s)' % (ctime(), user, data))
            else:
                sock.send('Nobody is chating with you. Maybe the one talked with you is talking with someone else')


def connect_thread(sock):
    """
    连接成功后需要输入一个用户名
    用户名类型：
        已存在
        （客户端直接输入ctrl+c退出）
        合法用户名
    :param sock: 客户端的socket
    :return:
    """
    # 设置用户名
    user = None
    while True:
        username = sock.recv(BUFSIZE)
        if not username:  # 客户端未输入用户名就退出
            print '客户端未设置用户名，并已退出'
            break
        if username in clients:
            sock.sendall('用户名重复，请重新输入：')
        else:
            sock.sendall('设置用户名成功')
            clients[username] = sock
            user = username
            break

    if not user:
        sock.close()
        return

    print '用户名为：{0}'.format(user)

    message_transform(sock, user)


if __name__ == '__main__':
    print '服务已启动，地址为{0}'.format(ADDR)
    while True:
        cs, addr = ss.accept()
        print '已与{0}建立连接'.format(addr)
        chat = threading.Thread(target=connect_thread, args=(cs,))
        chat.start()