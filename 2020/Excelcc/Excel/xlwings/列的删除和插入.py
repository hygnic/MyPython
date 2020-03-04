# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/3
# arcgis10.1 arcgis10.6

try:
	import xlwings as xw
except ImportError as e:
	print e
	
try:
	print "\n"
	app = xw.App(visible=False, add_book=False) # 只打开不新增工作簿
	app.display_alerts = False  # 关闭Excel弹窗
	app.screen_updating = False # 不更新屏幕显示
	xpath = u"表格删除.xlsx"
	wb = app.books.open(xpath)
	sheet1 = wb.sheets[0]
	v1 = sheet1.range("a1:a7").value
	print v1
	sheet1.range("a1").api.EntireRow.Delete()  # 删除该单元格所在的行
	sheet1.api.Rows(1).Insert()  # 插入一行
	
	
	wb.save("new")

finally:
	app.quit()
	print "\n close application"