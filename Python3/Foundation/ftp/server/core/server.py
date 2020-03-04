# User: hygnic
# Date: 2018/9/12
import socketserver
import json
from core import views
from config import settings

class MyFTPServer(socketserver.BaseRequestHandler):
    """
    服务器端
    """
    # 消息的转发，把任务转给views文件中对应的方法
    def handle(self):
        msg = self.my_recv()
        op_str = msg['operation']  #$ why number 2 dont work?
        # 反射
        if hasattr(views, op_str):
            func = getattr(views, op_str)
            ret = func(msg)
            self.my_send(ret)


    def my_recv(self):  # 派生方法
        """接收数据"""
        msg = self.request.recv(1024)
        msg = msg.decode(settings.code)
        msg = json.loads(msg)
        return msg

    def my_send(self, msg):
        """数据发送"""
        msg = json.dumps(msg).encode(settings.code)
        self.request.send(msg)



