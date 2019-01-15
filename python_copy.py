#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
拷贝、移动文件或文件夹
依赖：make_dir.py, coding_convert.py, exit_with_log.py
"""

import os
import sys
import shutil

from make_dir import make_dir
from coding_convert import str_to_unicode
from exit_with_log import exit_with_log

reload(sys)
sys.setdefaultencoding('utf-8')


def python_copy(copy_source, copy_target, mode='copy', ignore_errors=True, retry_count=1):
    """
    拷贝或移动文件、文件夹（移动会将源文件夹删除）
    :param str copy_source: 源文件（夹）
    :param str copy_target: 目标文件夹
    :param str mode: "copy": 拷贝；"move"：移动
    :param bool ignore_errors: True则忽略失败，False则失败退出
    :param int retry_count: 总尝试次数
    """
    copy_source = os.path.normpath(copy_source)
    copy_target = os.path.normpath(copy_target)
    copy_source = str_to_unicode(copy_source)
    copy_target = str_to_unicode(copy_target)
    print('[{0}]{1} --> {2}'.format(mode, copy_source, copy_target))

    count = 1
    is_error = False
    while count <= retry_count:
        try:
            if not os.path.exists(copy_target):
                make_dir(copy_target)

            if os.path.isdir(copy_source):
                copy_dir(copy_source, copy_target)

                if mode == 'move':
                    shutil.rmtree(copy_source, ignore_errors=True)

                # 如果不希望移动时将源文件夹删除，则重新建一个即可
                # if not os.path.exists(copy_source):
                #     make_dir(copy_source)
            else:
                shutil.copy2(copy_source, copy_target)
                if mode == 'move':
                    os.remove(copy_source)
            is_error = False
            break
        except Exception as e:
            is_error = True
            print('[{0} error]{1}'.format(mode, e))

        count += 1

    if (not ignore_errors) and is_error:
        exit_with_log('python_copy error exit')


def copy_dir(src_dir, dest_dir):
    """
    拷贝文件夹
    :param src_dir: 源文件夹路径
    :param dest_dir: 目标文件夹路径
    :return:
    """
    if not os.path.exists(dest_dir):
        make_dir(dest_dir)

    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            # 创建目标内部文件夹
            for dir_name in dirs:
                dest_dir_inside = os.path.join(dest_dir, dir_name)
                if not os.path.exists(dest_dir_inside):
                    make_dir(dest_dir_inside)

            # 拷贝文件
            for file_name in files:
                file_path = os.path.join(root, file_name)
                dest_dir_inside = dest_dir + root[len(src_dir): len(root)] + '/'
                shutil.copy2(file_path, dest_dir_inside)  # src: file; dest: dir


def main():
    src_dir = r'E:\Workspaces\copytest'
    dest_dir = r'E:\Workspaces\dir\fda1'
    python_copy(src_dir, dest_dir)


if __name__ == '__main__':
    main()
