# User: hygnic
# Date: 2018/9/8

# User: hygnic
# Date: 2018/9/8
import os
import time
from multiprocessing import Process


# help(os)
def func1(args):
    print(args)
    time.sleep(2)
    print('son process: ', os.getpid())


def func2(filename, content):
    with open(filename, 'w') as content_wp:
        content_wp.write(content)


if __name__ == '__main__':
    # 注册进程
    j_list = []
    for i in range(10):  # 开启多个子进程
        f1 = Process(target=func1, args=('*' * i,))  # 单个参数时有一个逗号，元组
        # p2 = Process(target=func, args=('实参', '实参2'))  通过这种方式开启多个子进程
        f1.start()  # 开启一个子进程 内部会调用run()方法
        j_list.append(f1)  # 表中全是一个个进程

    f2 = Process(target=func2, args=('info', 'func2 content'))
    f2.start()

    # print(j_list)
    # 阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程。将异步改为同步
    [f1.join() for f1 in j_list]  # 列表表达式
    print('Done! father process: ', os.getpid())
