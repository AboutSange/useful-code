#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = '\xcd\xa8\xb3\xa3\xc3\xbf\xb8\xf6\xcc\xd7\xbd\xd3\xd7\xd6\xb5\xd8\xd6\xb7(\xd0\xad\xd2\xe9/\xcd\xf8\xc2\xe7\xb5\xd8\xd6\xb7/\xb6\xcb\xbf\xda'
# a = s.encode('unicode_escape').decode('string_escape')
# b = repr(a)
# print unicode(eval(b),"gbk").encode('utf8')

# a = s.encode('raw_unicode_escape')
# b = repr(a)
# print unicode(eval(b),"gbk").encode('utf8')

print s.decode('gbk')