#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
将驼峰字符串转换成下划线分隔字符串
"""

import re


def hump_to_underline(hump_str):
    """
    Convert the hump  form string to an underscore
    :param str hump_str: hump  form string
    :return: All lowercase underlined string of letters
    :rtype: str
    """
    patt = re.compile(r'([a-z]|\d)([A-Z])')
    underline_str = re.sub(patt, r'\1_\2', hump_str).lower()
    return underline_str


def main():
    result = hump_to_underline('HelloWorld')
    print(result)


if __name__ == '__main__':
    main()
