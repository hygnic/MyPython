# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/30

"""锁的使用"""

from threading import Thread,RLock
import time
lock1 = RLock()
v= []
def func(arg):
	lock1.acquire()
	v.append(arg)
	time.sleep(0.01)
	# 从列表中获取东西时，如果没加锁，其他进程可能会同时操作，会导致其获取的数值与预想的不一致
	m = v[-1]
	print arg, m
	lock1.release()


for i in xrange(10):
	t = Thread(target=func, args=(i,))
	t.start()
