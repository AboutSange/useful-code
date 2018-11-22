#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
通过psutil模块获取CPU、内存、硬盘、网络等信息
原文：https://blog.csdn.net/bzfys/article/details/49817355
"""


import psutil
import datetime


#测试的时间
date=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print('Now time : %s' % date)

#使用用户
print('User : %s' % psutil.users())

#check cpu
#华丽的分割线
print('==================================CPU=======================================')

#检测CPU所有信息
print('CPU Ringing time : %s ' % psutil.cpu_times(percpu=True))

#检测CPU用户进程时间百分比
print('user : %s ' % psutil.cpu_times().user)

#检测IO等待
# print('IO wait : %s ' % psutil.cpu_times().iowait)

#检测idle占用百分比
print('idle : %s ' % psutil.cpu_times().idle)

#检测CPU逻辑个数
print('CPU logic : %s ' % psutil.cpu_count())

#检测CPU物理个数
print('CPU physical number : %s ' % psutil.cpu_count(logical=False))



#华丽的分割线
print('Memory')
print('===================================Memory====================================')
#check memory


#检测内存总量
mem=psutil.virtual_memory().total/1024/1024
print('Memory total : %s M' % mem)

#检测可用内存
mem=psutil.virtual_memory().available/1024/1024
print('Memory available : %s M' % mem)

#检测free内存
mem=psutil.virtual_memory().free/1024/1024
print('Memory free : %s M' % mem)

#检测已使用内存
mem=psutil.virtual_memory().used/1024/1024
print('Memory used : %s M' % mem)

#检测内存使用的比例
print('Percentage of usage : %s %%' % psutil.virtual_memory().percent)



print('===================================Swap=======================================')
#检测Swap所有信息

#检测swap总量
swap = psutil.swap_memory().total/1024/1024
print('Swap total : %s M ' % swap)

#检测swap free
swap = psutil.swap_memory().free/1024/1024
print('Swap free : %s M ' % swap)

#检测swap空闲
swap = psutil.swap_memory().free/1024/1024
print('Swap used : %s M ' % swap)

#检测swap使用量
swap = psutil.swap_memory().used/1024/1024
print('Swap used : %s M ' % swap)

#检测使用百分比
print('Percentage of usage : %s %%' % psutil.swap_memory().percent)

#系统从磁盘交换的字节数
swap = psutil.swap_memory().sin/1024/1024
print('Swap sin : %s M ' % swap)

#系统从磁盘交换的字节数
swap = psutil.swap_memory().sout/1024/1024
print('Swap sout : %s M ' % swap)



print('===================================Disk======================================')
#check disk
#查看磁盘空间使用情况
disk=psutil.disk_partitions()
for i in disk:
        print(i)
print
print

#查看IO读写信息
disk=psutil.disk_io_counters(perdisk=True)
print disk


print('==================================Network=====================================')
#check network
#查看每个网卡的状态
#for i in psutil.net_io_counters(pernic=True):
#       print(i)
print(psutil.net_io_counters(pernic=True))

