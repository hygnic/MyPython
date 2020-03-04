# User: hygnic
# Date: 2018/9/6
import socket
import time

sk = socket.socket()  # buy a phone
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 表示可重复利用一个端口，避免服务器重启的时候报address already in use 的错误
# sk.bind(('ip', 'port'))
sk.bind(('127.0.0.1', 8090))  # binding phone card
# noinspection PyArgumentList
sk.listen()  # monitor phone
conn, addr = sk.accept()  # answer the phone  connection, address
# 拿到连接（connection）后就使用连接通信
print(addr)


# conn.recv(1024)   # 加上这句就会出问题
ret = conn.recv(1024).decode('utf-8')  # 听别人说话（表示数据字节）
print(ret)  # 将服务器端接受到的数据打印出来

conn.send(b'hi')  # 和别人说话，必须传一个bytes类型，将数据传给客户端

ret = conn.recv(1024).decode('utf-8')
print(ret)

conn.send(bytes('大碗面'.encode('utf-8')))
# conn.send(bytes('大碗面', 'utf-8')) 效果同上

print('=' * 20)
# 持续3s给客户端发送时间
while True:
    msg = input('>>>')
    if msg == 'q':
        conn.send(bytes('程序结束', encoding='utf-8'))
        break
    else:
        while True:
            tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            conn.send(bytes(tim, encoding='utf-8'))
            time.sleep(3)


conn.close()  # 挂电话
sk.close()  # 关手机
