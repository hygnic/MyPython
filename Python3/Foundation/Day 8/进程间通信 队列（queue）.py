# User: hygnic
# Date: 2018/9/11
# IPC(inter_process communication)

import queue
"""
# help(queue)
# 队列中内置就有锁


d = queue.Queue(3)
d.put('lcc')  # 将数据放入队列
d.put('yq')
d.put('ys')
# d.put('ji') # 管道现在只能装3个，再往里面添加东西时会堵塞住
# d.get('ys')  # 移除并获取队列中的数据


print(d.get())
print(d.get())
print(d.get())
# print(d.get()) # 默认会堵住，因为队列已空
# print(d.get(0)) # 设置为0时，不会堵住了，继续往下执行，然后报错

# FIFO 管道
"""


from multiprocessing import Queue, Process

def producer(q):
    q.put('hello')

def consumer(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    p.start()
    p2 = Process(target=consumer, args=(q, ))
    p2.start()

# 实现了两个子进程之间的通信