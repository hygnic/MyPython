# User: hygnic
# Date: 2018/9/12
import socketserver, os, json, re
from config import settings

REQUEST_CODE = {
    '1001': 'cmd info',
    '1002': 'cmd ack',
    '2001': 'post info',
    '2002': 'ACK(可以开始上传)',
    '2003': '文件已近存在',
    '2004': '续传',
    '2005': '不续传',
    '3001': 'get info',
    '3002': 'get ack',
    '4001': '未授权',
    '4002': '授权成功',
    '4003': '授权失败'
}



class MultiServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes('欢迎登陆', 'utf-8'))
        obj = Action(conn)
        while True:
            client_bytes = conn.recv(1024)
            if not client_bytes:
                break
            client_str = str(client_bytes, encoding='utf-8')
            if obj.has_login:
                o = client_str.split('|', 1)
                if len(o) > 0: # 反射
                    func = getattr(obj, o[0])
                    func(client_str)
                else:
                    conn.sendall(bytes("输入格式有误", 'utf-8'))
            else:
                obj.login(client_str)

        conn.close()

class MultiServer(object):
    """创建多线程的TCP协议的服务器端"""
    # 支持多用户登陆
    def __init__(self):
        server = socketserver.ThreadingTCPServer(
            (settings.BIND_HOST, settings.PORT), MultiServerHandler)
        server.serve_forever()

class Action(object):
    def __init__(self, conn):
        self.conn = conn
        self.has_login = False
        self.username = None
        self.home = None   # 等待玩家登陆赋予家目录
        self.current_dir = None

    # def login(self, origin):
    #     self.conn.sendall(bytes('4001', 'utf-8'))
    #     while True:
    #         login_str = str(self.conn.recv(1024), encoding='utf-8')
    #         login_dict = json.loads(login_str)
    #         if login_dict['username'] == 'wupeiqi' and login_dict['pwd'] ==
    #             self.conn.sendall(bytes('4002', 'utf-8'))
    #             self.has_login = True
    #             self.username = 'wupeiqi'
    #             self.initialize() # 登陆成功，初始化成功
    #             break
    #         else:
    #             self.conn.sendall(bytes('4003', 'utf-8'))



    def initialize(self):
        self.home=os.path.join(settings.USER_HOME, self.username)
        self.current_dir = os.path.join(settings.USER_HOME, self.username)

    def cmd(self, origin):
        func, command = origin.split('|', 1)
        command_list = re.split('\s*', command,1)

        if command_list[0] == 'ls':
            if len(command_list) == 1:
                if self.current_dir:
                    command_list.append(self.current_dir)
                else:
                    command_list.append(self.home)
            else:
                if self.current_dir:
                    p = os.path.join(self.current_dir, command_list[1])
                else:
                    p = os.path.join(self.home, command_list[1])
                self.current_dir = p
                command_list[1] = p
        command = ' '.join(command_list)
        try:
            result_bytes = bytes('error cmd', encoding='utf-8 ')
        except:
            pass


    def post(self, origin):
        pass

    def get(self, origin):
        pass

    def exit(self, origin):
        pass
