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


def recv(cs, addr):
    """
    沟通线程
    :param cs: client socket
    :param addr: client addr
    :return:
    """
    while True:
        try:
            data = cs.recv(BUFSIZE)
            if not data:
                break

            print '[client]{0}: {1}'.format(addr, data)
        except Exception as e:
            print '客户端异常，已断开与{0}的连接，错误信息：{1}'.format(addr, e)
            break

    cs.close()

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ss.bind(ADDR)
ss.listen(3)  # backlog表示已完成(ESTABLISHED)且未accept的队列大小

print '服务已启动，地址为{0}'.format(ADDR)

while True:
    cs, addr = ss.accept()

    print '正在与{0}通信'.format(addr)

    t = threading.Thread(target=recv, args=(cs, addr))
    t.daemon = True
    t.start()

    while True:
        try:
            send_data = raw_input()
            if not send_data:
                break

            cs.sendall('{0}'.format(send_data))
        except Exception as e:
            print '客户端异常，已断开与{0}的连接，错误信息：{1}'.format(addr, e)
            break

ss.close()
