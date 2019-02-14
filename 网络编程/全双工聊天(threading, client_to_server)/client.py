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
    :param cs: server socket
    :param addr: client addr
    :return:
    """
    print '正在与{0}通信'.format(addr)

    while True:
        try:
            data = cs.recv(BUFSIZE)
            if not data:
                break

            print '[server]{0}: {1}'.format(addr, data)
        except Exception as e:
            print '服务器异常，已断开与{0}的连接，错误信息：{1}'.format(addr, e)
            break

    cs.close()


cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
cs.connect(ADDR)

print '已连接上{0}'.format(ADDR)

t = threading.Thread(target=recv, args=(cs, ADDR))
t.daemon = True
t.start()

while True:
    try:
        data = raw_input()
        if not data:
            break
        cs.sendall(data)
    except Exception as e:
        print '服务器异常，已断开与{0}的连接，错误信息：{1}'.format(ADDR, e)
        break
cs.close()

