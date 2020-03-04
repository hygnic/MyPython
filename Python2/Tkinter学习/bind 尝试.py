# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/23

# 将tkinter写成Tkinter可兼容Python 2.x
from Tkinter import *
class App(object):
	def __init__(self, master):
		self.master = master
		self.show = Label(self.master, width=30, bg='white', font=('times', 20))
		self.initWidgets()
	def initWidgets(self):
		self.show.pack()
		bn = Button(self.master, text= u'from event.widget')
		bn.pack(fill=BOTH, expand=YES)
		# 为左键单击事件绑定处理方法
		bn.bind('<Button-1>', self.one)
		# 为左键双击事件绑定处理方法
		bn.bind('<Double-1>', self.double)
	def one(self, event):
		self.show['text'] = u"左键单击:%s" % event.widget['text']
	def double(self, event):
		print(u"左键双击, 退出程序:", event.widget['text'])
		import sys; sys.exit()
root = Tk()
root.title('简单绑定')
App(root)
root.mainloop()