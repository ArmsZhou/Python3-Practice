#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-12-05 10:27:37
# @Author  : Arms (526923945@qq.com)
# @Link    : https://armszhou.github.io
# @Version : $Id$

from xlrd import open_workbook
import re
import os

workbook_name = '钱端(定制版)接口汇总.xlsx'
result_file_name = 'IID_Data'
result_file_path = '/'.join([os.getcwd(), result_file_name])


def build_IID_Data():
    wb = open_workbook(workbook_name)
    # 获取常规接口的 sheet
    sheet = wb.sheets()[0]

    with open(result_file_path, 'w') as f:
        for rownum in range(sheet.nrows):
            # 获取每行的前3列单元格
            rowvalue = '|'.join([sheet.cell(rownum, 0).value, sheet.cell(
                rownum, 1).value, sheet.cell(rownum, 2).value]) + '\n'
            f.writelines(rowvalue)

if __name__ == '__main__':
    build_IID_Data()
