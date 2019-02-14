#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Windows下会报错，因为Windows下select不支持文件描述符sys.stdin
"""

import socket
import sys
import select

reload(sys)
sys.setdefaultencoding('utf-8')

HOST = '127.0.0.1'
PORT = 12346
BUFSIZE = 1024
ADDR = (HOST, PORT)


cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
cs.connect(ADDR)

print '已连接上{0}'.format(ADDR)

inputs = [sys.stdin, cs]

while True:
    input_list, output_list, exception_list = select.select(inputs, [], [])
    for input_socket in input_list:
        if input_socket == cs:
            data = cs.recv(BUFSIZE)
            if not data:
                break
            print data
        else:
            data = raw_input()
            if not data:
                break
            cs.sendall(data)

cs.close()
