#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
格式化退出日志
"""

import sys

from log_print import log_print


def exit_with_log(log_str, is_exit=True, exit_code=-1, log_obj=None):
    """
    格式化退出日志
    :param str log_str: 退出日志
    :param bool is_exit: 是否退出
    :param int exit_code: 退出码
    :param obj log_obj: 日志对象
    :return:
    """
    big_info = '[error]' if is_exit else '[warning]'
    log_print('\r\n\r\n---------------------------------{0}---------------------------------'.format(big_info), log_obj=log_obj)
    log_print(log_str, log_obj=log_obj)
    log_print('-------------------------------------------------------------------------\r\n', log_obj=log_obj)
    if is_exit:
        sys.exit(exit_code)


def main():
    exit_with_log('再见来不及握手')
    print('done')

if __name__ == '__main__':
    main()
