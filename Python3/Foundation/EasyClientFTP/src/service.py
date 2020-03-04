# User: hygnic
# Date: 2018/9/12
import socket
import os
import sys
from config import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


# print(sys.path)
# print(settings.port)
def cmd(conn, inp):
    conn.sendall(bytes(inp, 'utf-8'))
    basic_info_bytes = conn.recv(1024)
    basic_info_bytes = str(basic_info_bytes, 'utf-8')
    if basic_info_bytes == '4001':
        login(conn)
    else:
        conn.sendall(bytes('ask', 'utf-8'))
        print(str(basic_info_bytes, 'utf-8'))


def post():
    pass



def get():
    pass



def help_info():
    print("""
            cmd|命令
            post|文件路径
            get|下载文件路径
            exit|退出
    """)


def execute(conn):
    choice_dict = {
        'cmd': cmd,
        'get': get,
        'post': post,
    }
    help_info()
    while True:
        # cmd | ls
        # post| 本地路径 服务器上路径
        inp = input('please input: ')
        if inp == 'help':
            help_info()
            continue
        choice = inp.split('|')[0]
        if choice == 'exit':
            return   # 在while 循环中加入一个return即可停止循环
        if choice in choice_dict:
            func = choice_dict[choice]
            func(conn, inp)


def main():
    ip_port = (settings.server, settings.port)
    conn = socket.socket()
    conn.connect(ip_port)
    welcome_bytes = conn.recv(1024)
    print(str(welcome_bytes, encoding='utf-8'))  # $　encode ?

    execute(conn)

    conn.close()
