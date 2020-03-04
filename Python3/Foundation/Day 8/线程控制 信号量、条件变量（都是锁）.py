# User: hygnic
# Date: 2018/9/11
import threading, time

"""
# 信号量 信号量是并列的几把锁
class myThread(threading.Thread):
    def run(self):
        semaphore.acquire()
        print(self.name)
        time.sleep(2)
        semaphore.release()


if __name__ == "__main__":
    semaphore = threading.Semaphore(5)  # 创建信号量，参数控制线程数量
    # semaphore = threading.BoundedSemaphore(5)  # 一样的
    t_list = []
    for i in range(40):
        t_list.append(myThread())
    for t in t_list:
        t.start()

# 用于连接数据库
"""

# 条件变量
    # 这类线程需要在满足条件时才能继续执行

    # wait()：条件不满足时调用，线程会释放锁并进入等待阻塞；
    # notify()：条件创造后调用，通知等待池激活一个线程；
    # notifyAll()：条件创造后调用，通知等待池激活所有线程

# 生产者和消费者模型

import threading, time
from random import randint


class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val = randint(0, 100)
            print('生产者', self.name, ":Append" + str(val), L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()  # 通知，激活wait()
                lock_con.release()
            time.sleep(3)


class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            # if lock_con.acquire(): # 两个都可以
            lock_con.acquire()
            if len(L) == 0:
                lock_con.wait()  # 阻塞
                print('不走这儿了')  # 在notify通知激活wait() 后，
                # 不会接着这儿走了，从第60行走
            print('消费者', self.name, ":Delete" + str(L[0]), L)
            del L[0]
            lock_con.release()
            time.sleep(0.25)


if __name__ == "__main__":

    L = []
    lock_con = threading.Condition()  # 创建一个条件变量的锁
    threads = []
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()
