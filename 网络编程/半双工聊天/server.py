#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
IP(网络地址+主机地址)
    A类：0.0.0.0到127.255.255.255，保留地址10.X.X.X, 127.0.01
    B类：128.0.0.0到191.255.255.255，保留地址172.16.X.X-172.31.X.X，特殊地址169.254.x.x
    C类：192.0.0.0到223.255.255.255，保留地址192.168.X.X
    D, E类广播地址：224.0.0.0---239.255.255.255，240.0.0.0---255.255.255.254

端口号范围[0, 65535]，系统端口号一般在[0, 1024]间，常用端口号有：
    20  ftp-data
    21  ftp
    22  ssh
    23  telnet
    25  smtp，简单邮件传输协议
    53  domain，域名服务
    80  http，超文本传输协议
    110 pop3，邮局协议3
    115 sftp，安全文件传输协议
    443 https，安全超文本传输协议

socket地址家族和套接字
    地址家族：
        AF_UNIX：基于文件
        AF_INET：面向网络
    套接字：
        SOCK_STREAM：TCP套接字，虚拟电路式，面向连接
        SOCK_DGRAM：UDP套接字，数据报式，无连接
"""

import socket
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

HOST = '127.0.0.1'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ss.bind(ADDR)
ss.listen(3)  # backlog表示已完成(ESTABLISHED)且未accept的队列大小

print '服务已启动，地址为{0}'.format(ADDR)

while True:
    cs, addr = ss.accept()

    print '正在与{0}通信'.format(addr)

    while True:
        try:
            data = cs.recv(BUFSIZE)
            if not data:
                break

            print '[client]{0}: {1}'.format(addr, data)

            send_data = raw_input('>')
            if not send_data:
                break

            cs.sendall('{0}'.format(send_data))
        except Exception as e:
            print '客户端异常，已断开与{0}的连接，错误信息：{1}'.format(addr, e)
            break

    cs.close()
ss.close()
