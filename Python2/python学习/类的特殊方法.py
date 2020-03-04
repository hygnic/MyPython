# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/24

class Bar(object):
	def __new__(cls, *args, **kwargs):
		print u"真正的构造方法"
		return object.__new__(cls)  # python内部创建一个当前类的对象
	
	# 初创时是空的
	
	def __init__(self):
		print "init"
	
	def __call__(self, *args, **kwargs):
		print "call"
		print(12, args, kwargs)  # (12, (1, 2, 3, 4), {'didi': 89})
	
	def __setitem__(self, key, value):
		print "setitem"
		a = int(key) * value
		print a  # 12
	
	def __enter__(self):
		print "want me exit?"
		return u"enter的返回值"
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		print u"我退出来"
	
	def test(self):
		pass


obj = Bar()
obj(1, 2, 3, 4, didi=89)  # (12, (1, 2, 3, 4), {'didi': 89})

obj["3"] = 4  # 12

with obj as f:
	print f
	print u"测试enter和exit"
# 输出：
# want me exit?
# enter的返回值
# 测试enter和exit
# 我退出来
