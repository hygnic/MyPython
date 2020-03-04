# User: hygnic
# Date: 2018/9/9

# 子进程转换为守护进程
import time
from multiprocessing import Process

def func():
    while True:
        print('sub process')
        time.sleep(0.5)

if __name__ == '__main__':
    p = Process(target=func)
    # 守护进程：在主进程结束时强行结束子子进程
    #          随着主进程的代码执行完毕而结束
    p.daemon = True # 设置子进程为守护进程
    p.start()
    i = 0
    while i<5:
        print('main process')
        time.sleep(0.5)
        i += 1