#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
from http://blog.sina.com.cn/s/blog_4b5039210100etpy.html
"""

from time import ctime

from Tkinter import *

from SimpleDialog import *

import socket

import thread

import sys


class PPChatservGUI(object):
    def __init__(self, host='localhost', port=7162):

        self.top = Tk()

        self.top.title('PPChat server v1.1')

        # 创建socket并绑定

        self.ChatSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ChatSerSock.bind((host, port))

        self.ChatSerSock.listen(5)

        # 预留功能菜单

        self.menubar = Menu(self.top)

        for item in ['menu1', 'menu2', 'menu3', 'menu4']:
            self.menubar.add_command(label=item)

        self.menubar.add_command(label='About', command=self.OnAbout)

        self.top['menu'] = self.menubar

        # 创建Frame

        self.frame = []

        self.frame.append(Frame())

        self.frame.append(Frame())

        # 消息输出列表框右边的滚动条

        self.slbar = Scrollbar(self.frame[0])

        self.slbar.pack(side=RIGHT, fill=Y)

        # 创建消息输出列表框，并绑定上面的滚动条

        self.MessageOut = Listbox(self.frame[0], height=25, fg='red')

        self.MessageOut['yscrollcommand'] = self.slbar.set

        self.MessageOut.pack(expand=1, fill=BOTH)

        self.slbar['command'] = self.MessageOut.yview

        self.frame[0].pack(expand=1, fill=BOTH)

        # 创建消息输入Entry

        self.MessageIn = Entry(self.frame[1], width=60, fg='red')

        self.MessageIn.pack(expand=1, fill=X, pady=10, padx=15)

        # 创建发送按钮

        self.sendMesgButton = Button(self.frame[1],

                                     text='Send',

                                     width=10,

                                     command=self.OnSendMessage)

        # self.sendMesgButton.bind("<Return>",self.SendMessageTo)

        self.sendMesgButton.pack(side=BOTTOM and RIGHT, padx=20, pady=10)

        # 创建退出按钮

        self.quitButton = Button(self.frame[1], text='Quit', width=10, command=self.OnQuit)

        self.quitButton.pack(side=RIGHT, padx=20, pady=10)

        self.frame[1].pack()

    # 发送消息

    def OnSendMessage(self):

        self.send_data = ''

        self.send_data = self.MessageIn.get()

        if self.send_data:
            self.MessageOut.insert(END, 'you said [%s]:' % ctime())

            self.MessageOut.insert(END, self.send_data)

            self.MessageOut.insert(END, '')

            self.MessageIn.delete(0, self.send_data.__len__())

            self.ChatClitSock.send(self.send_data)

    # socket 通信

    def SocketProc_recv(self):

        self.buffer = 1024

        self.MessageOut.insert(END, 'Waiting for connection...')

        while True:

            self.ChatClitSock, self.clit_addr = self.ChatSerSock.accept()

            self.MessageOut.insert(END, '....connected already....')

            while True:

                self.recv_data = self.ChatClitSock.recv(self.buffer)

                if not self.recv_data:
                    break

                self.MessageOut.insert(END, 'Your friend said  [%s]:' % ctime())

                self.MessageOut.insert(END, self.recv_data)

                self.MessageOut.insert(END, '')

            self.ChatSerSock.close()

            self.ChatClitSock.close()

    # 退出

    def OnQuit(self):

        self.ChatSerSock.close()

        self.top.quit()

    # 关于

    def OnAbout(self):

        pass

    # 多线程执行收发

    def mutiThread(self):

        thread.start_new_thread(self.SocketProc_recv, ())


def main():
    pp = PPChatservGUI()

    pp.mutiThread()

    mainloop()


if __name__ == '__main__':
    main()
