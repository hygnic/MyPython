# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/10/17

"""设置简单的button响应"""
import os
import Tkinter as tk
import sys


window = tk.Tk()
window.title(u"公示图大战分布图")
window.geometry("400x320")
# window.iconbitmap(default = r"toolbox.ico")

# 图形界面设置标签
var = tk.StringVar()
l = tk.Label(window, textvariable=var, text = u"公示图处理", bg = "red",
			 width = 8, height = 8)
l.pack()
getText = tk.Entry(window,show=None)
getText.pack()


hit_flag = False
def hit_b():
	global hit_flag
	if not hit_flag:
		hit_flag = True
		var.set("ni hao")
	else:
		var.set("")
		hit_flag = False
		
script_path2 = "gif_test1.py"
def func():
	msg = getText.get()
	# 使用CMD运行py程序
	os.system("python2" + " " + script_path2)
	file1 = open(msg,"w")
	writelist = sys.path
	file1.write(writelist)
	file1.close()


# 在窗口界面设置放置Button按键,连接函数hit_me
b1 = tk.Button(window, text='hit me', font= ('Arial', 12),
			  width=10, height=1, command = hit_b)
b2 = tk.Button(window, text='write txt', font= ('Arial', 12),
			   width=10, height=1, command = func)

b1.pack(side ="left")
b2.pack(side ="right")
# 主循环
window.mainloop()