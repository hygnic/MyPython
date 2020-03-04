# User: hygnic
# Date: 2018/9/11
import socket, json


class MySocketClient():
    def __init__(self):
        # establish a connection
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1', 8080))

    def mysend(self, msg):
        ret_json = json.dumps(msg)
        self.sk.send(ret_json.encode('utf-8'))

print('i\' m socket_client')