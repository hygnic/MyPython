# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/26
import time
def timer(func):
    """一个程序计时器"""
    def inner(*args,**kwargs):
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print "soeed time: ",t2
    return inner

# @timer
# def bar():
#     for i in xrange(200000):
#         print i
# s = bar()

def bar():
    for i in xrange(200000):
        print i
        
s =timer(bar)
s()

for xx in xrange(2,5):
    print xx