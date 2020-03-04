# User: hygnic
# Date: 2018/9/9
import socket
from multiprocessing import Process


def func(conn):
    while True:
        send_msg = ('EasyServerFTP is ok!').encode('utf-8')
        conn.send(send_msg)

        get_msg = conn.recv(1024).decode('utf-8')
        print(get_msg)
        # conn.close()


sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 9000))
sk.listen()

if __name__ == '__main__':
    while True:  # 实现并发，可连接多个client
        conn, addr = sk.accept()
        p = Process(target=func, args=(conn,))
        p.start()
    # sk.close()