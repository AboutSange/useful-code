#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
二分查找（折半查找）
条件：有序列表
时间复杂度：O(logn)
空间复杂度：O(1)
算法描述：
    查找过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜素过程结束；
    如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
    如果在某一步骤数组为空，则代表找不到。
"""

import codecs


def binary_search(key, lst):
    """
    列表的二分查找。
    :param key: 待查找的值
    :param lst: 有序列表
    :return: 索引位
    """
    # lo: low; hi: high
    lst_len = len(lst)  # 有序列表长度
    lo = 0  # 低位
    hi = lst_len -1  # 高位

    while lo <= hi:
        # 被查找的键要么不存在，要么必然存在lst[lo..hi]之中
        mid = lo + (hi - lo) // 2  # 中间位的索引
        if key < lst[mid]:
            hi = mid - 1
        elif key > lst[mid]:
            lo = mid + 1
        else:
            return mid

    return -1


def search_largeW():
    """
    读取文本文件largeT(100W个int值)，从中搜索值，并返回值所在行。如果没搜索到，则返回-1。
    """
    # 读取文本文件
    with codecs.open('largeW.txt', 'r', 'utf-8') as f:
        lst_raw = f.readlines()  # read cost: 1.199120044708252s

    # 将列表元素转换成int类型
    lst_int = [int(i) for i in lst_raw]  # str to int cost: 2.451245069503784s

    # 将列表排序，并保留排序前的索引
    lst_sorted_zip = sorted(zip(lst_int, range(len(lst_int))), key=lambda x: x[0])  # [(23, 0), (344, 1)]  lst_sorted_zip cost: 15.132513046264648s

    # 排序后的列表，不包含排序前的索引
    lst_sorted = [i[0] for i in lst_sorted_zip]  # lst_sorted cost: 3.146314859390259s
    # lst_sorted_2 = sorted(lst_int)  # 10.617061853408813

    # 搜索并返回排序后的索引
    index = binary_search(10, lst_sorted)  # binary_search cost: 0.0010001659393310547s

    # 计算排序前的索引
    index_new = lst_sorted_zip[index][1]

    # 返回值在文本所在行
    line = index_new + 1 if index_new != -1 else -1  # 5317578
    print(line)
    return line


def main():
    aa = [1, 4, 10, 34, 54, 100]
    print(binary_search(11, aa))


if __name__ == '__main__':
    main()
    # search_largeW()