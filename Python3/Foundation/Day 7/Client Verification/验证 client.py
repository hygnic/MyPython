# User: hygnic
# Date: 2018/9/7
import socket
import hmac

secret_key = b'egg'
sk = socket.socket()
sk.connect(('127.0.0.1', 8091))

msg = sk.recv(1024)

h = hmac.new(secret_key, msg)
digest = h.digest()
sk.send(digest)


sk.close()