# User: hygnic
# Date: 2018/9/9
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
while True:
    get_msg = sk.recv(1024).decode('utf-8')
    print(get_msg)

    send_msg = input('client>>>').encode('utf-8')
    sk.send(send_msg)

# sk.close()