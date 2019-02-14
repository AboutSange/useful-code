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


def Send(sock):
    while True:
        try:
            data = raw_input()
            sock.send(data)
            if data == 'Quit':
                break
        except KeyboardInterrupt:
            sock.send('Quit')
            break


def Recv(sock):
    while True:
        data = sock.recv(BUFSIZE)
        if data == 'Quit.':
            print('He/She logout')
            continue
        if data == 'Quit':
            break
        print '         %s' % data


if __name__ == '__main__':
    username = None
    while True:
        username = raw_input('Your name(press only Enter to quit): ')
        cs.sendall(username)
        if not username:
            break

        response = cs.recv(BUFSIZE)
        if response == '用户名重复，请重新输入：':
            continue
        else:
            break

    if not username:
        cs.close()

    recv_message = threading.Thread(target=Recv, args=(cs,))
    send_message = threading.Thread(target=Send, args=(cs,))
    send_message.start()
    recv_message.start()
    send_message.join()
    recv_message.join()
