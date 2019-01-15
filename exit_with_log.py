#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
格式化退出日志
"""

import sys


def exit_with_log(log_str, is_exit=True, exit_code=-1):
    """
    格式化退出日志
    :param str log_str: 退出日志
    :param bool is_exit: 是否退出
    :param int exit_code: 退出码
    :return:
    """
    big_info = '[error]' if is_exit else '[warning]'
    print('\r\n\r\n---------------------------------{0}---------------------------------'.format(big_info))
    print(log_str)
    print('-------------------------------------------------------------------------\r\n')
    if is_exit:
        sys.exit(exit_code)


def main():
    exit_with_log('再见来不及握手')
    print('done')


if __name__ == '__main__':
    main()
