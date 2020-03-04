# User: hygnic
# Date: 2018/9/7
import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8096))
while True:
    msg = input('>>>')
    if msg == 'q':
        break
    sk.send(bytes('Client2: '+msg, 'utf8'))
    # sk.send(msg.encode('utf-8'))

    ret = sk.recv(1024).decode('utf-8')
    print(ret)


# sk.send(bytes('无限连接', encoding='utf-8'))

sk.close()
