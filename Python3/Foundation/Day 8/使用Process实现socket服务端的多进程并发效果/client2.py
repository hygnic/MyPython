# User: hygnic
# Date: 2018/9/9
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8081))

sk.send(bytes('你好', 'utf-8'))

msg = sk.recv(1029).decode('utf-8')
print(msg)

sk.close()