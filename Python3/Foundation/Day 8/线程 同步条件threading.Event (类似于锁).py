# User: hygnic
# Date: 2018/9/11

# 同步条件
"""
条件同步和条件变量同步差不多意思，只是少了锁功能，
因为条件同步设计于不访问共享资源的条件环境。
event=threading.Event()：条件环境对象，初始值 为False.
"""
import threading,time

help(threading.Event)