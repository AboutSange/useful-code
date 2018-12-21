#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json
import codecs


def rename_directory(dir_path, add_str, type='after'):
    """
    将文件夹中所有文件和文件夹名加前缀或后缀
    :param str dir_path: 文件夹路径
    :param str add_str: 需要增加的字符串
    :param str type: 前缀还是后缀，默认后缀。'before': 前缀; 'after': 后缀
    """
    name_list = os.listdir(dir_path)  # dir_path中的文件名和目录名列表（不包括子目录中的文件或目录）

    for name in name_list:
        path = os.path.join(dir_path, name)

        # type输入不正确则默认为after
        if type == ur'before':
            path_new = os.path.join(dir_path, ur'{0}{1}'.format(add_str, name))
        else:
            path_new = ur'{0}{1}'.format(path, add_str)

        if os.path.isdir(path):
            rename_directory(path, add_str, type)
        os.rename(path, path_new)


def replace_keyword(dir_path, replace_dict):
    """
    将文件夹中的文件名和文件夹名中的关键字改成目标关键字（不包括后缀名），如果包含目标关键字就跳过，异常（被占用等）也跳过

    标志：
        重命名成功：[success]<原始路径> === <新路径>
        重命名失败：[error]<原始路径> === <新路径> === <错误信息>
        跳过：[pass]<原始路径>
        未改变：[unchanged]<原始路径>

    :param dir_path: 文件夹路径
    :param dict replace_dict:
        {
            "a": "wo",
            "b": "ye",
            "c": "hen",
            "d": "wu",
            "e": "nai",
            "f": "ya",
            "g": "fuck"
        }
    """
    name_list = os.listdir(dir_path)  # dir_path中的文件名和目录名列表（不包括子目录中的文件或目录）
    target_keyword_list = replace_dict.values()  # 目标关键字列表，用来判断是否跳过
    target_keyword_dict = replace_dict.items()  # 目标关键字列表，用来判断是否跳过

    for name in name_list:
        name_root, name_ext = os.path.splitext(name)  # 区分后缀名
        path = os.path.join(dir_path, name)
        # 判断是否包含目标关键字，包含则跳过
        need_pass = False  # 是否跳过
        for target_keyword in target_keyword_list:
            if target_keyword in name_root:
                need_pass = True
                break
        if need_pass:
            print ur'[pass]{0}'.format(path)
            continue

        # 如果是目录，则需要递归，将目录中的文件或目录重命名之后再重命名本目录
        if os.path.isdir(path):
            replace_keyword(path, replace_dict)

        # 获取新名字
        name_root_new = name_root
        for keyword, target_keyword in target_keyword_dict:
            name_root_new = name_root_new.replace(keyword, target_keyword)

        # 重命名
        path_new = os.path.join(dir_path, ur'{0}{1}'.format(name_root_new, name_ext))
        if path_new == path:
            print ur'[unchanged]{0}'.format(path)
        try:
            os.rename(path, path_new)
            print ur'[success]{0} === {1}'.format(path, path_new)
        except Exception as e:
            print ur'[error]{0} === {1} === {2}'.format(path, path_new, e)


def main():
    # # 加前缀或后缀 rename_directory
    # dir_path = ur'E:\python27\workspaces\rename\ceshi新建文件夹'  # 目标文件夹路径
    # add_str = ur'_bak'  # 前缀或后缀字符串
    # type = ur'before'  # 类型：before: 前缀  after: 后缀
    # rename_directory(dir_path, add_str, type)

    # # 替换关键字 replace_keyword
    dir_path = ur'E:\Workspaces\新建文件夹 (10)'  # 目标文件夹路径
    json_path = ur'replace_list.json'  # json文件的路径，该json文件用来存放关键字和目标关键字字典
    # 读取json文件
    with codecs.open(json_path, 'r', 'utf-8') as f:
        replace_dict = json.load(f)
    replace_keyword(dir_path, replace_dict)


if __name__ == '__main__':
    main()
