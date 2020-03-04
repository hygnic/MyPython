# User: hygnic
# Date: 2018/9/8
import os
import time
from multiprocessing import Process

"""
# 方法一

# help(os)
def func(args):
    print(args)
    time.sleep(3)
    print('子进程: ', os.getpid())


if __name__ == '__main__':
    # 注册进程
    p = Process(target=func, args=('实参',))  # 单个参数时有一个逗号，元组
    # p2 = Process(target=func, args=('实参', '实参2'))  通过这种方式开启多个子进程
    p.start()  # 开启一个子进程  内部会调用run()方法
    # 阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程。将异步改为同步
    p.join()  # 感知一个子进程的结束，相当于将func方法拼接到该位置
    print('父进程: ', os.getpid())
"""


# 方法二 面向对象

class LServe(Process):
    def __init__(self, a1, a2):
        super().__init__()  # 要执行父类中的初始化参数才行
        self.arg1 = a1
        self.arg2 = a2

    def run(self):  # 必须实现
        print(os.getpid())
        print(self.pid)
        print(self.arg1)
        print(self.arg2)


if __name__ == '__main__':
    p1 = LServe('参数1', '参数2')
    p1.start()  # 内部会调用run()方法
