# User: hygnic
# Date: 2018/9/10
import threading
import time

"""
# 方法一
# 直接创建线程
begin = time.time()
def foo(a):
    time.sleep(1)
    print('-%s-' % a)


def bar(a):
    time.sleep(1)
    print('-%s-' % a)


t1 = threading.Thread(target=foo, args=('func 1',))
t1.start()
t2 = threading.Thread(target=bar, args=('func 2',))
t2.start()

#  实现了多线程，并发
end = time.time()
print(end - begin)

"""
# 方法二 面向对象

# 利用类创建线程

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.n = name

    def run(self):
        print('%s is running' % self.n)
        time.sleep(2)


if __name__ == '__main__':
    t = MyThread('lcc')
    t.start()
    r2 = MyThread('yq')
    r2.start()  # 使用start() 来启动类中的方法run（）
