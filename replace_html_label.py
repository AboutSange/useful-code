#!/usr/bin/env python
# -*- coding:utf-8 -*-


__author__ = 'CQC'
import re


# 处理页面标签类
class Tool(object):
    # 去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    # 将多行空行删除
    removeNoneLine = re.compile('\n+')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        # strip()将前后多余内容删除
        return x.strip()


def main():
    html = r'            发财了发财了，萌新这笔钱怎么花比较值啊？<br><img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=b976fcaad839b6004dce0fbfd9513526/06af02fa513d2697f556f71458fbb2fb4216d8b2.jpg" size="116550" changedsize="true" width="560" height="297" size="116550">'
    print '[old]{0}'.format(html)
    tool = Tool()
    new_html = tool.replace(html)
    print '[new]{0}'.format(new_html)


if __name__ == '__main__':
    main()
