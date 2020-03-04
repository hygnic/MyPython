# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/5

class Foo:
	pass

obj1 = Foo()
print(Foo)
# 实例化对象
print(obj1)

class Bar:
	def __str__(self):
		return 'cccc'
	pass

obj = Bar()
print(Bar)
# 实例化对象，print会调用__str__方法，所见非所得
	# 看上去是字符串，实际上是对象
print(obj)

def outer():
	a=10
	def inner():
		print(a)
	return inner

fn = outer()
fn()

