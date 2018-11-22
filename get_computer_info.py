#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
获取计算机信息、操作系统信息、python信息
原文：https://www.cnblogs.com/black-mamba/p/7061352.html
"""

"""
python中，platform模块给我们提供了很多方法去获取操作系统的信息
如：
    import platform
    platform.platform()        #获取操作系统名称及版本号，'Linux-3.13.0-46-generic-i686-with-Deepin-2014.2-trusty'  
    platform.version()         #获取操作系统版本号，'#76-Ubuntu SMP Thu Feb 26 18:52:49 UTC 2015'
    platform.architecture()    #获取操作系统的位数，('32bit', 'ELF')
    platform.machine()         #计算机类型，'i686'
    platform.node()            #计算机的网络名称，'XF654'
    platform.processor()       #计算机处理器信息，''i686'
    platform.uname()           #包含上面所有的信息汇总，('Linux', 'XF654', '3.13.0-46-generic', '#76-Ubuntu SMP Thu Feb 26 18:52:49 UTC 2015', 'i686', 'i686')

    还可以获得计算机中python的一些信息：
    import platform
    platform.python_build()
    platform.python_compiler()
    platform.python_branch()
    platform.python_implementation()
    platform.python_revision()
    platform.python_version()
    platform.python_version_tuple()
"""

import socket
import uuid
import getpass
import platform
import urllib2
import time


def get_computer_hostname():
    """获取计算机名"""
    return socket.gethostname()


def get_computer_ip():
    """获取计算机IP"""
    host_name = get_computer_hostname()
    ip = socket.gethostbyname_ex(host_name)[2][0]
    return ip


def get_computer_mac():
    """获取计算机MAC地址（多网卡就不准了）"""
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e: e+2] for e in range(0, 11, 2)])


def get_user():
    """获取用户名"""
    return getpass.getuser()


def get_server_info():
    """获取远程服务器信息"""
    sock = urllib2.urlopen('http://www.baidu.com')
    info = sock.headers.values()
    return info


def get_current_time():
    """获取当前时间"""
    return time.strftime(r'%Y-%m-%d %H:%M:%S', time.localtime())


def get_platform():
    '''获取操作系统名称及版本号'''
    return platform.platform()


def get_version():
    '''获取操作系统版本号'''
    return platform.version()


def get_architecture():
    '''获取操作系统的位数'''
    return platform.architecture()


def get_machine():
    '''计算机类型'''
    return platform.machine()


def get_node():
    '''计算机的网络名称'''
    return platform.node()


def get_processor():
    '''计算机处理器信息'''
    return platform.processor()


def get_system():
    '''获取操作系统类型'''
    return platform.system()


def get_uname():
    '''汇总信息'''
    return platform.uname()


def get_python_build():
    ''' the Python build number and date as strings'''
    return platform.python_build()


def get_python_compiler():
    '''Returns a string identifying the compiler used for compiling Python'''
    return platform.python_compiler()


def get_python_branch():
    '''Returns a string identifying the Python implementation SCM branch'''
    return platform.python_branch()


def get_python_implementation():
    '''Returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.'''
    return platform.python_implementation()


def get_python_version():
    '''Returns the Python version as string 'major.minor.patchlevel'
    '''
    return platform.python_version()


def get_python_revision():
    '''Returns a string identifying the Python implementation SCM revision.'''
    return platform.python_revision()


def get_python_version_tuple():
    '''Returns the Python version as tuple (major, minor, patchlevel) of strings'''
    return platform.python_version_tuple()


def show_computer_all_info():
    print('获取计算机名 : {}'.format(get_computer_hostname()))
    print('获取计算机IP : {}'.format(get_computer_ip()))
    print('获取计算机MAC地址（多网卡就不准了） : {}'.format(get_computer_mac()))
    print('获取用户名 : {}'.format(get_user()))
    print('获取远程服务器信息 : {}'.format(get_server_info()))
    print('获取当前时间 : {}'.format(get_current_time()))


def show_os_all_info():
    '''打印os的全部信息'''
    print('获取操作系统名称及版本号 : {}'.format(get_platform()))
    print('获取操作系统版本号 : {}'.format(get_version()))
    print('获取操作系统的位数 : {}'.format(get_architecture()))
    print('计算机类型 : {}'.format(get_machine()))
    print('计算机的网络名称 : {}'.format(get_node()))
    print('计算机处理器信息 : {}'.format(get_processor()))
    print('获取操作系统类型 : {}'.format(get_system()))
    print('汇总信息 : {}'.format(get_uname()))


def show_python_all_info():
    '''打印python的全部信息'''
    print('The Python build number and date as strings : {}'.format(get_python_build()))
    print('Returns a string identifying the compiler used for compiling Python : {}'.format(get_python_compiler()))
    print('Returns a string identifying the Python implementation SCM branch : {}'.format(get_python_branch()))
    print('Returns a string identifying the Python implementation : {}'.format(get_python_implementation()))
    print('The version of Python ： {}'.format(get_python_version()))
    print('Python implementation SCM revision : {}'.format(get_python_revision()))
    print('Python version as tuple : {}'.format(get_python_version_tuple()))


def main():
    print('计算机信息:')
    show_computer_all_info()

    print('#' * 50)

    print('操作系统信息:')
    show_os_all_info()

    print('#' * 50)

    print('计算机中的python信息：')
    show_python_all_info()

if __name__ == '__main__':
    main()