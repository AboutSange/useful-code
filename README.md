# useful-code
常用代码仓库

1. [url_reserved_char_encode.py](url_reserved_char_encode.py): 将url保留字符转成ASCII
```
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
```

2. [decorator_use_in_class.py](decorator_use_in_class.py): 在类中对方法使用的装饰器，自动打印方法开始和结束日志
```
[Demo.func.start.....]
Hello decorator
[Demo.func.end.....]
```

3. [log_print.py](log_print.py): 日志打印（日志对象或print）
4. [run_cmd.py](run_cmd.py): 执行命令行
5. [coding_convert.py](coding_convert.py): 编码转换（str_to_unicode, unicode_to_str）
6. [python_copy.py](python_copy.py): 拷贝、移动文件或文件夹
```
[copy]E:\Workspaces\copytest --> E:\Workspaces\dir\fda
[move]E:\Workspaces\copytest --> E:\Workspaces\dir\fda
```

7. [exit_with_log.py](exit_with_log.py): 格式化退出日志
8. [make_dir.py](make_dir.py): 更安全地创建目录（解决多个进程同时创建一个目录时异常报错的问题）
9. [get_computer_info.py](get_computer_info.py): 获取计算机信息、操作系统信息、python信息
```
计算机信息:
获取计算机名 : PC
获取计算机IP : 192.168.1.100
获取计算机MAC地址（多网卡就不准了） : 88:88:88:88:88:88
获取用户名 : admin
获取远程服务器信息 : ['0xb1077a510000aafd', 'chunked', 'BAIDUID=027C97DE06C3CD0A0D6892C21F68078E:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, BIDUPSID=027C97DE06C3CD0A0D6892C21F68078E; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, PSTM=1542875151; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com, delPer=0; path=/; domain=.baidu.com, BDSVRTM=0; path=/, BD_HOME=0; path=/, H_PS_PSSID=1438_21090_27245_27543; path=/; domain=.baidu.com', 'Thu, 22 Nov 2018 08:25:15 GMT', 'Accept-Encoding', 'BWS/1.1', 'close', 'baidu+750539e23ac0c0d42914db0a157d54b9', 'private', 'Thu, 22 Nov 2018 08:25:51 GMT', 'CP=" OTI DSP COR IVA OUR IND COM "', 'text/html', '1', 'IE=Edge,chrome=1']
获取当前时间 : 2018-11-22日 16:25:51
##################################################
操作系统信息:
获取操作系统名称及版本号 : Windows-7-6.1.7600
获取操作系统版本号 : 6.1.7600
获取操作系统的位数 : ('64bit', 'WindowsPE')
计算机类型 : AMD64
计算机的网络名称 : PC
计算机处理器信息 : Intel64 Family 6 Model 58 Stepping 9, GenuineIntel
获取操作系统类型 : Windows
汇总信息 : ('Windows', 'admin', '7', '6.1.7600', 'AMD64', 'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel')
##################################################
计算机中的python信息：
The Python build number and date as strings : ('default', 'May 23 2015 09:44:00')
Returns a string identifying the compiler used for compiling Python : MSC v.1500 64 bit (AMD64)
Returns a string identifying the Python implementation SCM branch : 
Returns a string identifying the Python implementation : CPython
The version of Python ： 2.7.10
Python implementation SCM revision : 
Python version as tuple : ('2', '7', '10')
```

10. [get_computer_info_by_psutil.py](get_computer_info_by_psutil.py): 通过psutil模块获取CPU、内存、硬盘、网络等信息
```
Now time : 2018-11-17 14:04:55
User : [suser(name='admin', terminal=None, host='0.0.0.0', started=1542589458.0, pid=None)]
==================================CPU=======================================
CPU Ringing time : [scputimes(user=11279.80859375, system=8193.4375, idle=421462.96875, interrupt=161.8510284423828, dpc=395.66534423828125), scputimes(user=1044.9415283203125, system=1701.53125, idle=438189.0625, interrupt=918.0191040039062, dpc=213.5341796875), scputimes(user=8241.611328125, system=7445.625, idle=425248.15625, interrupt=42.978275299072266, dpc=79.63851165771484), scputimes(user=1010.44970703125, system=778.3125, idle=439146.5, interrupt=32.40140914916992, dpc=42.120269775390625), scputimes(user=7386.95947265625, system=6316.0, idle=427232.15625, interrupt=34.46062088012695, dpc=59.28037643432617), scputimes(user=377.75640869140625, system=214.8125, idle=440342.4375, interrupt=16.941709518432617, dpc=26.27056884765625), scputimes(user=5865.6845703125, system=4986.875, idle=430082.3125, interrupt=25.100561141967773, dpc=56.95596694946289), scputimes(user=1215.107421875, system=1567.6875, idle=438151.96875, interrupt=12.433279991149902, dpc=13.166484832763672)] 
user : 36422.3164062 
idle : 3459855.5 
CPU logic : 8 
CPU physical number : 4 
Memory
===================================Memory====================================
Memory total : 16271 M
Memory available : 5839 M
Memory free : 5839 M
Memory used : 10431 M
Percentage of usage : 64.1 %
===================================Swap=======================================
Swap total : 32541 M 
Swap free : 21823 M 
Swap used : 21823 M 
Swap used : 10718 M 
Percentage of usage : 32.9 %
Swap sin : 0 M 
Swap sout : 0 M 
===================================Disk======================================
sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')
sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed')
sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed')


{'PhysicalDrive0': sdiskio(read_count=748116, write_count=2966206, read_bytes=28479472128L, write_bytes=56418669056L, read_time=2994L, write_time=3586L)}
```

11. [hump_to_underline.py](hump_to_underline.py): 将驼峰字符串转换成下划线分隔字符串
12. [replace_html_label.py](replace_html_label.py): 替换掉html中多余空格、换行、标签等，保留文字

```
[old]            发财了发财了，萌新这笔钱怎么花比较值啊？<br><img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=b976fcaad839b6004dce0fbfd9513526/06af02fa513d2697f556f71458fbb2fb4216d8b2.jpg" size="116550" changedsize="true" width="560" height="297" size="116550">
[new]发财了发财了，萌新这笔钱怎么花比较值啊？
```