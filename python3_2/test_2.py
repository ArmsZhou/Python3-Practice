#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-11-29 10:11:27
# @Author  : Arms (526923945@qq.com)
# @Link    : https://armszhou.github.io
# @Version : $Id$

import os

# 标识符与关键字
# 引导字符 + 后续字符
# 引导字符：字母、下划线(_)或大多数非英文语言字母
# 后续字符：任意非空字符
# 标识符是大小写敏感的

# 整型

# 二进制   0b 或者 0B
# 八进制   0o 或者 0O
# 十六进制 0x 或者 0X

print(bin(1980))
# 0b11110111100
print(oct(1980))
# 0o3674
print(hex(1980))
# 0x7bc
print(int('7bc', 16)) # int(s, base) 将字符串 s 转换为整数，base 表示对应的进制
# 1980
print(int('3674', 8))
# 1980
print(int('11110111100', 2))
# 1980

# 布尔类型
# True
# False

# 浮点型
# 浮点型的相等性比较是不可靠的
# float
# complex
# decimal.Decimal 计算时运行速度较慢，但精度高于以上两种，适用于财政计算

print(float())
# 0.0

# 如何进行浮点数相等比较
import sys
def equal_float(a, b):
    return abs(a - b) <= sys.float_info.epsilon

# 16进制转换
s = 14.25.hex()
print(s) # 0x1.c800000000000p+3
f = float.fromhex(s)
print(f) # 14.25
t = f.hex()
print(t) # 0x1.c800000000000p+3
# 指数使用 p 表示，因为16进制中 e 表示一个有效的16进制数字

# 复数
# 存放着一堆浮点数，一个表示实数部分，一个表示虚数部分。
# 复数的两个部分都以属性名的形式存在，分别为 real 和 imag。
# 数学家使用字母 i 表示根号-1，但 Python 遵循工程传统，使用 j 表示。
z = -89.5 + 2.125j
print(z.real, z.imag)

# 精准的十进制数字
# 使用 Decimals
import decimal
a = decimal.Decimal(9876)
b = decimal.Decimal('50000.0123456789876543210')
print(a + b) # 59876.0123456789876543210
# decimal.Decimal() 函数接受一个整数或者字符串作为参数，不接受浮点数，因为浮点数是不准确的。
# 可以使用 decimal.Decimal 的 from_float 函数将 float 转换为最接近的 decimal 类型。
print(decimal.Decimal.from_float(0.12345))
# 0.123450000000000004174438572590588591992855072021484375

# 字符串
print(str())
# ' '
a = 'a'
# " "
b = "b"
# """ """  三引号直接使用换行而无需使用 \n 转义
c = """abcdefg
higklmn
opqrst
uvwxyz
"""
print(c)

# r"str" 引导的字符串无需转义
import re
phoneRegex = re.compile(r"^((?:[0\d+[]])?\s*\d+(?:.-\d+)?)$")

# 如果要写一个长字符串，跨越了两行但是不使用三引号则可以
t = "abcedfghijklmnopqrst" + \
    "uvwxyz"
# abcedfghijklmnopqrstuvwxyz
s = ("abcedfghijklmnopqrst"
     "uvwxyz")
# abcedfghijklmnopqrstuvwxyz

# ord() 获取某个字符的整数值
print(ord('A'))
# 65

# 分片与步距
# []
# seq[start]
# seq[start:end] 包含 satrt 不包含 end
# seq[start:end:step] 包含 satrt 不包含 end
# seq 可以是任意的序列，如列表、字符串或元组。
s = 'abcdef'
print(s[0])
print(s[-1])
print(s[0:5])
print(s[:5])    #忽略时 start 为0
print(s[0:])    #忽略时 end 为 len(s)
print(s[:])     #都忽略时 等价于 s[0:len(s)]
print(s[0:len(s)])

# a
# f
# abcde
# abcde
# abcdef
# abcdef
# abcdef

# 使用 step 时，step 不能为0
# 忽略 start 则 start 为0，除非 step 是负值。同理忽略 end 则 end 为 len(s),除非 step 是负值。 step == -1 则相当于翻转序列。
s = 'he ate camel food'
print(s[::-1])
print(s[::-2])
# doof lemac eta eh
# do ea t h

# 常用方法
# join
t = ['a', 'b', 'c']
print(' '.join(t))
print('-'.join(t))
# a b c
# a-b-c

# reversed
s = 'abc'
print("".join(reversed(s)))
print(s[::-1])
# cba
# cba

# * 操作符提供了赋值功能
s = '=' * 5
print(s)
# =====
s *= 10
print(s)
# ==================================================

s = 'it is a <tag> in this string'

# find(t, start , end)    返回 t 在 s 中最左位置，如果没有返回 -1
print(s.find('tag'))
print(s.find('notfound'))
# 9
# -1

# index(t, start , end)   返回 t 在 s 中最左位置，如果产生 valueError 异常
print(s.index('tag'))
# print(s.index('notfound'))
# 9
# Traceback (most recent call last):
#   File "test_2.py", line 170, in <module>
#     print(s.index('notfound'))
# ValueError: substring not found

# 想想为什么 index() 会比 find() 好？

# count(t, start , end)  返回字符串 s 中子字符串 t 出现的次数
print(s.count('is', 2, len(s)))
# 2
# 等价于
print(s[2:].count('is'))
# 2

# partition(t) 返回包含3个字符串的元组 (字符串 s 在 t 左边的部分, t, 字符串 s 在 t 右边的部分)，如果没有则返回 (s,"","")
s = 'ab/cd'
print(s.partition('/'))
print(s.partition('-'))
# ('ab', '/', 'cd')
# ('ab/cd', '', '')

# split(t, n) 使用 t 在字符串 s 中进行分割 n 次，并返回一个列表。如果 t 不指定则在空白处分割，如果 n 不指定则尽可能分割多次。
s = '1980-11-28'
print(s.split('-'))
print(s.split())
s = '1980 11 28'
print(s.split('-'))
print(s.split())
# ['1980', '11', '28']
# ['1980-11-28']
# ['1980 11 28']
# ['1980', '11', '28']

# 使用 str.format() 方法进行字符串格式化
print('The novel {0} was published in {1}'.format('Hard Times', 1970))
# The novel Hard Times was published in 1970
# 如果需要在格式化字符串中包含花括号，则需要将其复写
print('{{{0}}} {1}'.format("i'm in braces", "i'm not"))
# {i'm in braces} i'm not

# 使用字段名来格式化参数
print('{who} turned {age} this year'.format(who='She', age=88))
# She turned 88 this year
print('The {who} wan {0} last week'.format(12, who='boy'))
# The boy wan 12 last week
# 可以看到关键字参数总是在位置参数后

# 字段名可以引用集合数据类型
stock = ['paper', 'envelopes', 'notepads', 'pens', 'paper clips']
print('We have {0[1]} and {0[2]} in stock'.format(stock))
# We have envelopes and notepads in stock
# 这里的0引用的是位置参数，如果有多个位置参数则依次排列
stock0 = ['paper', 'envelopes', 'notepads']
stock1 = ['pens', 'paper clips']
print('We have {0[0]} and {1[0]} in stock'.format(stock0, stock1))
# We have paper and pens in stock

