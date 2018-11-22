#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
日志打印
"""


def log_print(log_str='', log_obj=None):
    """
    日志打印
    :param log_str: 需要打印的字符串
    :param log_obj: 日志对象，如果为None，则print
    :return:
    """
    if log_obj == None:
        print(log_str)
    else:
        log_obj.info(log_str)


def main():
    log_print('hello log')


if __name__ == '__main__':
    main()
