#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
二分查找
"""


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
        # 被查找的键要么不存在，要么必然存在a[lo..hi]之中
        mid = lo + (hi - lo) // 2  # 中间位的索引
        if key < lst[mid]:
            hi = mid
        elif key > lst[mid]:
            lo = mid
        else:
            return mid

    return -1


def main():
    aa = [1, 4, 10, 34, 54, 100]
    print(binary_search(10, aa))


if __name__ == '__main__':
    main()
