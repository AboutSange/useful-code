#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
编码转换（str_to_unicode, unicode_to_str）
"""

import sys


def str_to_unicode(str1, encoding='default', debug=False):
    """
    将字符串转换成unicode编码格式
    :param str1: 需要转换编码的字符串本串
    :param encoding: 字符串编码。default, utf-8, gbk, etc.
    :param bool debug:  是否打印日志
    :return: unicode编码的字符串
    """
    if not isinstance(str1, unicode):
        encoding = encoding.lower()
        if encoding == 'default':
            encoding_list = ['utf-8', 'gbk', sys.getfilesystemencoding()]
        else:
            encoding_list = [encoding]

        for enc in encoding_list:
            try:
                str1 = str1.decode(enc)
                break
            except Exception as e:
                if debug:
                    print('[error]str_to_unicode: decode {0} to unicode failed'.format(enc))
                    print(e)
                pass

    return str1


def unicode_to_str(str1, encoding='system', debug=False):
    """
    将unicode字符串转换成encoding编码格式
    :param str1: 需要转换编码的字符串本串
    :param encoding: 字符串编码。system, utf-8, gbk, etc.
    :param bool debug:  是否打印日志
    :return: encoding编码的字符串
    """
    if isinstance(str1, str):
        encoding = encoding.lower()
        if encoding == 'system':
            enc = sys.getfilesystemencoding()
        else:
            enc = encoding

        try:
            str1 = str1.encode(enc)
        except Exception as e:
            if debug:
                print('[error]unicode_to_str: encode unicode to {0} failed'.format(enc))
                print(e)
            pass

    return str1


def main():
    demo_str = r'This is 中文 Mareike Böhmer_pillows'
    print(type(demo_str))

    unicode_str = str_to_unicode(demo_str)
    print(type(unicode_str))


if __name__ == '__main__':
    main()
