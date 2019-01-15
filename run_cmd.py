#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
执行命令行
依赖：coding_convert.py
"""

import sys
import subprocess
from coding_convert import str_to_unicode

reload(sys)
sys.setdefaultencoding('utf-8')


def run_cmd(cmd_str, shell=True, ignore_errors=False, retry_count=1):
    """
    执行命令行。
    :param cmd_str: 命令行
    :param shell: if shell is True, the specified command will be executed through the shell
    :param ignore_errors: 是否忽略错误
    :param retry_count: 重试次数
    :return:
    """
    cmd_str = str_to_unicode(cmd_str)
    print('cmd...{0}'.format(cmd_str))

    count = 1
    result_str = ''
    result_code = 0

    while count <= retry_count:
        cmdp = subprocess.Popen(cmd_str, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=shell)
        # cmdp.stdin.write('y/n')

        while True:
            result_line = cmdp.stdout.readline()
            if result_line:  # not EOF
                result_line = result_line.strip()
                if result_line:  # not empty line
                    result_line = str_to_unicode(result_line)
                    print('{0}'.format(result_line))
            else:
                # wait process end
                while cmdp.poll() is None:
                    pass
                break

        result_str = cmdp.stdout.read()
        result_str = str_to_unicode(result_str)
        result_code = cmdp.returncode

        # function retry needs
        if result_code == 0:
            break
        count = count + 1

    print('result_str...{0}'.format(result_str))
    print('result_code...{0}'.format(result_code))

    if not ignore_errors:
        if result_code != 0:
            print('run_cmd error exit')
            sys.exit(result_code)

    return result_code, result_str


def main():
    run_cmd(r'ipconfig /all')


if __name__ == '__main__':
    main()
