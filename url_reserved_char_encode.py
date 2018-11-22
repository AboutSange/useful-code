#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
功能：将url保留字符转成ASCII（摘抄自urllib.py）
    reserved = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" | "$" | ","

结果：
;  %3B
/  %2F
?  %3F
:  %3A
@  %40
&  %26
=  %3D
+  %2B
$  %24
,  %2C
   %20
"""


def encode_all():
    """
    将所有字符encode
    :return:
    """
    always_safe = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                   'abcdefghijklmnopqrstuvwxyz'
                   '0123456789' '_.-')
    _safe_map = {}
    for i, c in zip(xrange(256), str(bytearray(xrange(256)))):  # zip: 打包成元组的列表
        _safe_map[c] = c if (i < 128 and c in always_safe) else '%{:02X}'.format(i)  # key：字符  value：在url中显示的字符/字节码

    return _safe_map


def main():
    safe_map = encode_all()

    char_list = [';', '/', '?', ':', '@', '&', '=', '+', '$', ',', ' ']
    for char in char_list:
        print('{}  {}'.format(char, safe_map.get(char)))


if __name__ == '__main__':
    main()
