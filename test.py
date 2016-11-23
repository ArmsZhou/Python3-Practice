#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-11-23 14:01:24
# @Author  : Arms (526923945@qq.com)
# @Link    : https://armszhou.github.io
# @Version : $Id$

import os

text = 'abcde'
print(text[1])
# text[1] = 'B' 错误，在 python 中 str 类型和基本数值类型一旦设定就不可变的

# 单元素元组
route = (1,)
print(route, type(route))
# 空元组
route = ()
print(route, type(route))

# 单元素列表
route = [1,]
print(route, type(route))
# 空列表
route = []
print(route, type(route))

# 元组是不可变的，列表是可变的
a = (1, 2, 3)
b = [1, 2, 3]
# a[0] = 4 错误
b[0] = 4

# 逻辑操作符
# is 用于比较左右两端的对象引用(即变量)是否指向同一个对象
a = ['Retetion', 3, None]
b = ['Retetion', 3, None]
print(a is b) # False
b = a
print(a is b) # True
# == >= <= > < != 操作符左右两边对象类型要一样
c = ['Retetion', 3, None]
print(a == c) # True
print(0 <= 1 <= 2) # True 可以结链比较

# in, not in 对于序列或者集合类型，如字符串、列表、元组或字典
p = (4, 'frog', 9, -32, 9, 2)
print(2 in p) # True
print('dog' not in p) # True
# 思考：in 操作对于列表或者元组是线性搜索，数据量大时速度比较慢。对字典使用 in 就会很快。

# and or 注意返回的不是布尔值，而是决定结果的操作数。not 总是返回布尔值
two = 2
five = 5
zero = 0
print(two and five) # 5
print(five and two) # 2
print(zero and two) # 0
print(zero or two) # 2
print(two or zero) # 2
print(zero and two) # 0
print(two and zero) # 0
print(not two) # False
print(not zero) # True

# if
lines = 100
if lines < 100:
    print('small')
elif lines < 1000:
    print('medium')
else:
    print('large')

# while
num = 0
while num < 10:
    num = num + 1

# for ... in
for x in range(1, 10):
    print(x)
