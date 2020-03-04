# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/23

import openpyxl

wb = openpyxl.load_workbook(u"新建工作表 - 副本.xlsx")
s = wb["Sheet1"]

print s