# User: hygnic
# Date: 2018/9/7
import socket
import hmac  # 使用hashlib也是可以的
import os

secret_key = b'egg'

sk = socket.socket()
sk.bind(('127.0.0.1', 8091))
sk.listen()


def check_conn(conn):
    msg = os.urandom(32)
    conn.send(msg)  # os.urandom(32) 转换为字节bytes,且这个函数每次执行的结果会变
    h = hmac.new(secret_key, msg)  # hmac.new()  # 你想进行加密的bytes
    digest = h.digest()  # h.digest()  # 密文
    client_digest = conn.recv(1024)
    return hmac.compare_digest(digest, client_digest)  # 将两个密文进行比较，True, False


conn, addr = sk.accept()
res = check_conn(conn)
if res:
    print('合法的客户端')
    conn.close()
else:
    print('不合法的客户端')

sk.close()