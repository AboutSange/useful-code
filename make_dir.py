#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
更安全地创建目录（解决多个进程同时创建一个目录时异常报错的问题）
"""

import os


def make_dir(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            print(e)
            if not os.path.exists(path):
                os.makedirs(path)


def main():
    make_dir('d:/all pass')

if __name__ == '__main__':
    main()
