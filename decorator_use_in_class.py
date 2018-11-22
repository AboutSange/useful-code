#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
在类中对方法使用的装饰器，自动打印方法开始和结束日志
"""


def decorator_use_in_class(f):
    def wrapper(self, *args, **kwargs):
        log_info_start = r'[{}.{}.start.....]'.format(self.__class__.__name__, f.__name__)
        log_info_end = r'[{}.{}.end.....]'.format(self.__class__.__name__, f.__name__)
        print(log_info_start)
        out = f(self, *args, **kwargs)
        print(log_info_end)
        return out
    return wrapper


class Demo(object):
    @decorator_use_in_class
    def func(self):
        print('Hello decorator')


def main():
    d = Demo()
    d.func()


if __name__ == '__main__':
    main()
