# User: hygnic
# Date: 2018/9/11
import threading, time


class myThread(threading.Thread):
    def doA(self):
        lockA.acquire()
        print(self.name, "gotlockA", time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name, "gotlockB", time.ctime())
        lockB.release()
        lockA.release()

    def doB(self):
        lockB.acquire()
        print(self.name, "gotlockB", time.ctime())
        time.sleep(2)
        lockA.acquire()
        print(self.name, "gotlockA", time.ctime())
        lockA.release()
        lockB.release()

    def run(self):
        self.doA()
        self.doB()


if __name__ == "__main__":

    lockA = threading.Lock()
    lockB = threading.Lock()

    # lock = threading.RLock() # 递归锁，万用锁 递归锁是锁中锁
                                    # 递归锁就是用来解决死锁问题的
    # 详见 https://www.cnblogs.com/yuanchenqi/articles/5733873.html
    threads = []
    for i in range(5):
        threads.append(myThread())
    for t in threads:
        t.start()
    for t in threads:
        t.join()  # 等待线程结束，后面再讲。
