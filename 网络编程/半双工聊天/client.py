#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

HOST = '127.0.0.1'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
cs.connect(ADDR)

print '已连接上{0}'.format(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    cs.sendall(data)
    rdata = cs.recv(BUFSIZE)
    if not rdata:
        break
    print '[server]{0}: {1}'.format(ADDR, rdata)

cs.close()
