#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
服务器用来中转和保存关系
"""


import socket
import sys
import threading
import re
import copy
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
user_room_dict = {}  # username --> room, 记录用户名与room的关系
room_sock_dict = {}  # 记录房间与sock的关系，{room: [sock1, sock2]}


def message_transform(sock, addr, user, room):
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
    :param room:
    :return:
    """
    friends_sock_list = copy.copy(room_sock_dict[user_room_dict[user]])
    friends_sock_list.remove(sock)

    def _quit():
        if user in user_room_dict:
            data = 'Quit.'  # Quit.
            for s in friends_sock_list:
                s.sendall(data)
            friends_sock_list.remove(sock)
            del user_room_dict[user]
        del user_sock_dict[user]
        sock.close()
        print '{0}已退出房间{1}'.format(user, room)

    while True:
        try:
            data = sock.recv(BUFSIZE)
        except Exception as e:
            print e
            _quit()
            break
        print '[{0}]room {1} {2} {3}: {4}'.format(ctime(), room, addr, user, data)
        if not data or data == 'Quit':
            sock.sendall(data)
            _quit()
            break
        else:
            for s in friends_sock_list:
                s.sendall('[{0}]room {1} {2}: {3}'.format(ctime(), room, user, data))


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

    # 加入房间
    room = None
    while True:
        try:
            room = sock.recv(BUFSIZE)
        except Exception as e:
            print e
            print '客户端{0}未加入房间，并已退出'.format(addr)
            break
        if not room:  # 客户端加入房间就退出
            print '客户端{0}未加入房间，并已退出'.format(addr)
            break

        sock.sendall('加入房间 {0} 成功'.format(room))
        user_room_dict[user] = room
        if room in room_sock_dict:
            room_sock_dict[room].append(sock)
        else:
            room_sock_dict[room] = [sock]
        break

    if not room:
        sock.close()
        return

    message_transform(sock, addr, user, room)


if __name__ == '__main__':
    print '服务已启动，地址为{0}'.format(ADDR)
    while True:
        cs, addr = ss.accept()
        print '已与{0}建立连接'.format(addr)
        chat = threading.Thread(target=connect_thread, args=(cs, addr))
        chat.start()