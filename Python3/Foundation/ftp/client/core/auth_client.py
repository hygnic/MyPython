# User: hygnic
# Date: 2018/9/11
from core.socket_client import MySocketClient
import json


class Auth:
    """
    用于做登录和注册
    """

    # 单例模式，防止连续登录而创建多个socket连接
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance

    def __init__(self):
        self.socket = MySocketClient()  # 拿到了sk 连接
        self.username = None

    def login(self):
        username = input('username: ')
        password = input('password: ')
        # some system can't recognize space, so don't input space just in case
        if username.strip() and password.strip():
            self.socket.mysend({'username': 'alex',
                            'password': 'alex3714', 'operation': 'login' })
        ret = self.socket.sk.recv(1024)  # 获得登录结果

    def register(self):
        username = input('username: ')
        password1 = input('password: ')
        password2 = input('ensure_password: ')
        if username.strip() and password1.strip() and password1 == password2:
            self.socket.mysend({'username': 'alex',
                            'password': 'alex3714', 'operation': 'register'})

        ret = self.socket.sk.recv(1024)  # 获得注册结果


print('i\'m auth_client')