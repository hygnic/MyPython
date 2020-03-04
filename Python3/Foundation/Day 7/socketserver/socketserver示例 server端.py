import socketserver


class Server(socketserver.BaseRequestHandler):  # $ 必须继承BaseRequestHandler
    def handle(self):       # 必须有handle方法
        # self.request # self.request 相对于一个conn
        # print(self.request.recv(1024).decode('utf-8'))
        while True:
            msg = self.request.recv(1024).decode('utf-8')
            print(msg)
            if msg == 'q':
                break
            info = input('>>>')
            self.request.send(info.encode('utf-8'))


if __name__ == '__main__':
    # 设置allow_reuse_address允许服务器重用地址
    # socketserver.TCPServer.allow_reuse_address = True

    # thread 线程
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8096), Server)
    # 永远的启动一个线程
    server.serve_forever() # 让server永远运行下去，除非强制停止程序
