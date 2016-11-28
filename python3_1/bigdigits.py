#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-11-24 14:22:59
# @Author  : Arms (526923945@qq.com)
# @Link    : https://armszhou.github.io
# @Version : $Id$

import sys

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
#获取命令选中的第2个参数
    digits = sys.argv[1]
    row = 0
    while row < 7:  #因为我们使用7行的星号来表示一个数字
        line = ""
        column = 0
        while column < len(digits): #len(digits)获取是的字符串长度
            number = int(digits[column])    #半第2个参数中的字符转换成数字
            digit = Digits[number]  #取得大数字对象
            # 对比 * 并替换为对应数字
            d = 0
            while d < len(digit[row]):
                c = digit[row][d]
                if c == '*':
                    line += str(number)
                else:
                    line += c
                d += 1
            line += "  "   #打印大数字的第row行
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
