# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/21
# import xlwings as xw
#
# # 读取Excel
# try:
# 	app=xw.App(visible=False,add_book=False)
# 	app.display_alerts=False # 关闭Excel弹窗
# 	app.screen_updating=False
#
# 	xpath = u"xwings示例.xls"
# 	wb = app.books.open(xpath)	# <Book [XXXX.xlsx]>
# 	sheet1 = wb.sheets[0]	# <Sheet [XXXX.xlsx]Sheet1>
# 	v1 = sheet1.range("a1").value	# 'xxxx'
# 	v2 = sheet1.range("a1:a8").value	# list
# 	sheet1.range("a1:a5").value = "hh3333rrr"
# 	sheet1.delet() # 删除表单
#
# except:
# 	print "error!"
# else:
# 	wb.save("123")  # save as
# 	# wb.close()
# 	app.quit()
#
# finally:
# 	app.quit()




