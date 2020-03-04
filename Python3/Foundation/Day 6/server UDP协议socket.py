# User: hygnic
# Date: 2018/9/7
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)  # Datagram
sk.bind(('127.0.0.1', 8080))
while True:
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))

    info = input('>>>EasyServerFTP say:').encode('utf-8')
    sk.sendto(info, addr)

sk.close()

# udp的server 不需要进行监听也不需要建立连接
# 在发送信息的时候会自带地址信息
