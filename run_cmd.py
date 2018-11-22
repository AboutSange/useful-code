#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
执行命令行
"""

import sys
import subprocess

from log_print import log_print
from coding_convert import str_to_unicode
from exit_with_log import exit_with_log


def run_cmd(cmd_str, shell=False, ignore_errors=False, retry_count=1, log_obj=None):
    """
    执行命令行。
    注意：根据启动的进程的poll()判断程序是否结束，小部分概率会出现程序结束但poll()没有返回值（returncode）的情况，导致死循环（此种情况，则需用run_cmd_new）
    :param cmd_str: 命令行
    :param shell: if shell is True, the specified command will be executed through the shell
    :param ignore_errors: 是否忽略错误
    :param retry_count: 重试次数
    :param log_obj: 日志对象
    :return:
    """
    cmd_str = str_to_unicode(cmd_str)
    log_print('cmd...{0}'.format(cmd_str), log_obj=log_obj)

    count = 1
    result_str = ''
    result_code = 0

    while count <= retry_count:
        cmdp = subprocess.Popen(cmd_str, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=shell)
        # cmdp.stdin.write('y/n')

        while cmdp.poll() == None:
            result_line = cmdp.stdout.readline().strip()
            result_line = result_line.decode(sys.getfilesystemencoding())
            if result_line:
                log_print('{0}'.format(result_line), log_obj=log_obj)

        result_str = cmdp.stdout.read()
        result_code = cmdp.returncode

        # function retry needs
        if result_code == 0:
            break
        count = count + 1

    log_print('result_str...{0}'.format(result_str), log_obj=log_obj)
    log_print('result_code...{0}'.format(result_code), log_obj=log_obj)

    if not ignore_errors:
        if result_code != 0:
            exit_with_log('run_cmd error exit', exit_code=result_code)

    return result_code, result_str


def run_cmd_new(cmd_str, shell=False, log_obj=None):
    """
    执行命令行。当run_cmd出现死循环时的替换方案，不用poll()，无法获取returncode
    :param cmd_str: 命令行
    :param shell: if shell is True, the specified command will be executed through the shell
    :param log_obj: 日志对象
    :return:
    """
    cmd_str = str_to_unicode(cmd_str)
    log_print('cmd...{0}'.format(cmd_str), log_obj=log_obj)

    cmdp = subprocess.Popen(cmd_str, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=shell)
    # cmdp.stdin.write('y/n')

    while True:
        result_line = cmdp.stdout.readline()
        if result_line:  # not EOF
            result_line = result_line.strip()
            if result_line:  # not empty line
                log_print('{0}'.format(result_line), log_obj=log_obj)
        else:
            break

    return True


def main():
    run_cmd(r'calc')


if __name__ == '__main__':
    main()
