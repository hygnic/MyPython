# User: hygnic
# Date: 2018/9/6
import socket

sk = socket.socket()  # 买手机
sk.connect(('127.0.0.1', 8090))  # 获取服务器的地址，即拨别人的号

sk.send(b'hello')

# sk.recv(1024)  加上这句就会出问题
ret = sk.recv(1024)
print(ret.decode('utf-8'))

sk.send(bytes('中午吃什么', encoding='utf-8'))

ret = sk.recv(1024)
print(ret.decode('utf-8'))

# 持续接受时间
while True:
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
    if ret == '程序结束':
        break



sk.close()
