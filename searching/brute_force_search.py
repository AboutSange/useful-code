#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
暴力搜索
"""

import codecs


def brute_force_search(key, lst):
    """
    暴力搜索。
    :param key: 待查找的值
    :param lst: 有序列表
    :return: 索引位
    """
    for index, ele in enumerate(lst):
        if ele == key:
            return index
    return -1


def search_largeT():
    """
    读取文本文件largeT(1000W个int值)，从中搜索值，并返回值所在行。如果没搜索到，则返回-1。
    """
    # 读取文本文件
    with codecs.open('largeT.txt', 'r', 'utf-8') as f:
        lst_raw = f.readlines()  # read cost: 1.048105001449585s

    # 将列表元素转换成int类型
    lst_int = [int(i) for i in lst_raw]  # str to int cost: 2.3842380046844482s

    # 搜索并返回在lst_raw的索引
    index = brute_force_search(10, lst_int)  # brute_force_search cost: 0.026002883911132812s

    # 返回值在文本所在行
    line = index + 1 if index != -1 else -1
    print(line)
    return line


def main():
    aa = [1, 4, 10, 34, 54, 100]
    brute_force_search(10, aa)

if __name__ == '__main__':
    main()
    # search_largeT()