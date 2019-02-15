#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import sys
import threading

reload(sys)
sys.setdefaultencoding('utf-8')

HOST = '127.0.0.1'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
cs.connect(ADDR)
print '已连接上聊天服务器'


def send_thread(sock):
    while True:
        try:
            data = raw_input()
            sock.send(data)
            if data == 'Quit':
                break
        except KeyboardInterrupt:
            sock.send('Quit')
            break


def recv_thread(sock):
    while True:
        data = sock.recv(BUFSIZE)
        if data == 'Quit.':
            print('您的一位好友已退出聊天')
            continue
        if data == 'Quit':
            break
        print data


if __name__ == '__main__':
    username = None
    while True:
        username = raw_input('请输入您的用户名(只按Enter则退出)：')
        cs.sendall(username)
        if not username:
            break

        response = cs.recv(BUFSIZE)
        print response
        if response == 'REUSE':
            continue
        else:
            break

    room = None
    while True:
        room = raw_input('请输入您要加入的房间(只按Enter则退出)：')
        cs.sendall(room)
        if not room:
            break

        response = cs.recv(BUFSIZE)
        print response
        if response:
            break

    if not username or not room:
        cs.close()
    else:
        send_message = threading.Thread(target=send_thread, args=(cs,))
        recv_message = threading.Thread(target=recv_thread, args=(cs,))
        send_message.start()
        recv_message.start()
        send_message.join()
        recv_message.join()
