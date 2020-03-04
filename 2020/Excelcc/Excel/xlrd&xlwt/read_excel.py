# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/20
import xlrd,xlwt

def read():
	# 读取excel
	xlsx = xlrd.open_workbook(u"新建工作表.xlsx")
	print xlsx #<xlrd.book.Book object at 0x055429F0>
	# 获取sheetd的两种方式
	table = xlsx.sheet_by_index(0) # sheet1 = xlsx.sheet_by_name("sheet1")
	# 获取单元格内容的3种方式
	print table.cell_value(0,0) # this is the way the world ends
	print table.cell(0,0).value # this is the way the world ends
	# 行列
	print table.row(0)[0] # text:u'this is the way the world ends'
	print table.row(0)[0].value # this is the way the world ends

def write():
	# 写出
	new_workbook = xlwt.Workbook()
	worksheet = new_workbook.add_sheet("sheet1") # k
	worksheet.write(0,0,"hello")
	new_workbook.save(u"读出.csv")
	


