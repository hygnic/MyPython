# User: hygnic
# Date: 2018/9/11
import threading
import time

n = 100
def addnum():
    global n  # 全局变量
    # n -=1
    print('ok')   # 锁外照样执行，在等待锁中的IO操作时执行

    lc.acquire()  # 上锁  使锁中的代码执行完毕在切换线程
    temp = n
    time.sleep(0.05)
    n = temp - 1
    lc.release()  # 解锁


lc = threading.Lock()  # 定义一把锁
all_thread = []
for i in range(100):
    t = threading.Thread(target=addnum)
    t.start()
    all_thread.append(t)

for t in all_thread:  # 等待所有线程执行完毕,要是不加join的
    # 话会导致 可能部分线程没有执行完毕，但是已经执行 print代码。
    t.join()
print(n)

# for i in range(100):
#     addnum()
# print(n)
