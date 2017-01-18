#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-11-30 10:41:43
# @Author  : Arms (526923945@qq.com)
# @Link    : https://armszhou.github.io
# @Version : $Id$

import os

# 序列类型
# 序列类型支持关系操作符（in）,大小计算函数（len()）,分片([]),并且是可以迭代的。
# Python 提供了5种内置序列类型，bytearray、bytes、str、list、tuple。

# 元组
# 元组是不变的
print(tuple())
print(())
print((1,))
# ()
# ()
# (1,)

# 使用 + 拼接和使用 * 赋值
a = (1, 2, 3)
a *= 5
print(a)
# (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
a = (1, 2, 3)
a += (5,)
print(a)
# (1, 2, 3, 5)

# 命名的元组
# 可以提供更清晰、便利的操作
import collections
Sale = collections.namedtuple(
    'Sale', 'productid customerid date quantity price')
sales = []
sales.append(Sale(432, 921, '2008-09-14', 3, 7.99))
sales.append(Sale(419, 874, '2008-09-15', 1, 18.49))
print(sales)
# [
# Sale(productid=432, customerid=921, date='2008-09-14', quantity=3, price=7.99),
# Sale(productid=419, customerid=874, date='2008-09-15', quantity=1, price=18.49)
# ]
total = 0
for sale in sales:
    total = sale.quantity * sale.price
print('Total ${0:.2f}'.format(total))
# Total $18.49
# 相比较
print('productid {0}'.format(sales[0].productid))
# 更清晰
print('productid {0[0].productid}'.format(sales))

# 列表
print(list())
print([])
# []
# []

# 序列拆分操作符 *
first, *rest = [9, 2, -4, 8, 7]
print('first is {0}; rest is {1}'.format(first, rest))
# first is 9; rest is [2, -4, 8, 7]

first, *rest = (9, 2, -4, 8, 7)
print('first is {0}; rest is {1}'.format(first, rest))
# first is 9; rest is [2, -4, 8, 7]

first, *rest = 'abcde'
print('first is {0}; rest is {1}'.format(first, rest))
# first is a; rest is ['b', 'c', 'd', 'e']

# 当*出现在赋值操作的左边时，用作拆分操作符，出现在其他位置（比如函数调用内）时，若用作单值操作符，则代表拆分操作符；若用作二进制操作符，则代表多复制操作符。

# 通过对特定索引位置处的对象进行赋值，可以对列表中的单个数据项进行替换
# 通过将 iterable 赋值给分片，可以替换整个分片，并且分片与 iterable 并不必须是等长的。
L = ['A', 'B', 'C', 'D', 'E']
# 当分片起点、终点一样时，是插入操作
L[2:2] = ['X', 'Y']
print(L)
# ['A', 'B', 'X', 'Y', 'C', 'D', 'E']
# 当起点、终点不一样时，是替换操作
L = ['A', 'B', 'C', 'D', 'E']
L[2:3] = ['X', 'Y']
print(L)
# ['A', 'B', 'X', 'Y', 'D', 'E']
L = ['A', 'B', 'C', 'D', 'E']
L[2:5] = ['X', 'Y']
print(L)
# ['A', 'B', 'X', 'Y']

# 替换列表中的偶数为0
L = [1,2,3,4,5,6,7,8,9]
L[1::2] = [0]*(len(L[1::2]))
print(L)
# [1, 0, 3, 0, 5, 0, 7, 0, 9]

# 列表内涵(即列表生成式)
# 最简单的形式
# [item for item in iterable]
# 其他形式
# [expression for item in iterable]
# [expression for item in iterable if condition]

# 求指定时间段1990 - 1940的闰年
leaps = [leap for leap in range(1900, 1940) if (leap % 4 == 0 and leap %100 !=0) or (leap % 400 == 0)]
print(leaps)
# [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936]

# 集合类型
# {}
# set 和 frozenset
# 只有可哈希运算的对象可以添加到集合中，即该对象包含一个特殊方法__hash()__。

# 非空集合可以不使用 set() 函数创建，空集合必须使用 set() 函数创建。
print(set())
# set()

# 集合常要用来删除重复数据项
print(set('apple'))
print(set('aple'))
print({'e','p','l','a'})
# {'l', 'p', 'a', 'e'}
# {'l', 'p', 'a', 'e'}
# {'l', 'p', 'a', 'e'}

# 集合操作
A = set('pecan')
B = set('pie')
print(A | B) # 并集
print(A & B) # 交集
print(A - B) # 差集
print(A ^ B) # 对称差
# {'i', 'a', 'n', 'p', 'e', 'c'}
# {'p', 'e'}
# {'n', 'c', 'a'}
# {'i', 'a', 'n', 'c'}

# 集合常见使用场景
# 1.进行快速的成员关系测定
# 2.确保没有处理重复的数据
# 3.删除不需要的数据项

# 集合内涵
# 格式:
# {expression for item in iterable}
# {expression for item in iterable if condition}
# 使用的是大括号 {}

# 固定集合
# 一旦创建后就不能改变的集合
# 只能通过 frozenset() 函数创建
print(frozenset())
# frozenset()

# 如果使用二元操作符应用于集合和固定集合，则产生结果的数据类型与左边的操作数的数据类型一致。
# 固定集合 二元操作符 集合 ==》 固定集合
# 集合 二元操作符 固定集合 ==》 集合
S = set('abcde')
F = frozenset('defgh')
print(S & F)
print(F & S)
# {'d', 'e'}
# frozenset({'d', 'e'})

# 映射类型
# 映射是健值数据项的组合，并提供了存取数据项及其健值的方法。

# 字典
# 只有可哈希运算的对象可以作为字典的健，如固定类型 float、frozenset、int、str 以及 tuple
# 可变数据类型则不可以，如 set、list、dict

print(dict())
# {}
