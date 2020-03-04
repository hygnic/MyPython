# User: hygnic
# Date: 2018/9/15
# 事件：通过一个信号 来控制 多个进程 同时 执行或者阻塞

from multiprocessing import Event, Process
"""
# 一个信号可以使所有的进程都进入阻塞状态
# 也可以控制所有的进程解除阻塞
# 一个事件被创建之后，默认是阻塞状态

e = Event() # 创建了一个事件，默认被设置成阻塞
print(e.is_set())  # 查看一个事件的状态
e.set() # 将状态改为TRUE，这时才可以打印出 123456
# e.clear  # 将这个事件的状态改为False
e.wait()  # 依据e.is_set()的状态来决定是否阻塞
                # False 阻塞
print(123456)
"""

# 红绿灯问题
import time, random
def cars(e, i):
    if not e.is_set():
        print('car%s stop' % i)
        # else:
        e.wait() # 用来给汽车传递指令
    print('car%s run' % i)


def light(e):
    while True:
        if  not e.is_set(): # True
            print('\033[32m绿灯亮了\033[0m')
            e.set()  #　True

        else:
            e.clear() # false
            print('\033[31m红灯亮了\033[0m')
        time.sleep(2)


if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e, ))  # target=light() 也可以
    traffic.start()

    for i in range(100):
        car = Process(target=cars, args=(e, i))
        car.start()
        time.sleep(random.random()) # 0-1 sec
