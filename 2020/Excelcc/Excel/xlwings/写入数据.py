# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/4
# python2
# 直接写入数据不会重置excel的样式

import xlwings as xw
try:
	app = xw.App(visible=False, add_book=False)
	app.display_alerts = False
	app.screen_updating = False
	wb = app.books.open("new.xlsx")
	sheet1 = wb.sheets[0]
	sheet1.range("b1").value = "78"
	wb.save()
finally:
	app.quit()