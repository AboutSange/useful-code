#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Windows下会报错，因为Windows下select不支持文件描述符sys.stdin
可能可以用winapi中的GetStdHandle(STD_INPUT_HANDLE) 解决
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


ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ss.bind(ADDR)
ss.listen(3)  # backlog表示已完成(ESTABLISHED)且未accept的队列大小

inputs = [sys.stdin, ss]

print '服务已启动，地址为{0}'.format(ADDR)

while True:
    cs, addr = ss.accept()

    print '正在与{0}通信'.format(addr)

    inputs.append(cs)

    while True:
        input_list, output_list, exception_list = select.select(inputs, [], [])
        for input_socket in input_list:
            if input_socket == cs:  # 处理客户端的消息
                data = cs.recv(BUFSIZE)
                if not data:
                    inputs.remove(cs)
                    break
                print data
            else:  # 处理服务器端的消息
                data = raw_input()
                if not data:
                    inputs.remove(cs)
                    break
                cs.sendall(data)

    cs.close()
ss.close()
