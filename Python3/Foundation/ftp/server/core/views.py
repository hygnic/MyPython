# User: hygnic
# Date: 2018/9/12
import os, pickle
from core.user import User
from config import settings


def login(msg):
    print(msg)


def register(msg):
    """登录认证
     1.创建一个该用户的家目录,并记录下来
     2.把用户名和密码写进userinfo文件里，记录用户名
     3.记录用户的的磁盘配额
     4.记录文件大小
     5.记录用户当前所在的目录
    """
    user_obj = User(msg['username'])  # 记录用户的信息在内存里 # 传入name参数
    pickle_path = os.path.join(settings.pickle_path, msg['username'])
    with open(pickle_path, 'wb') as f:
        pickle.dump(user_obj, f)
    os.mkdir(user_obj.home)  # 创建属于这个用户的家目录 在home文件夹下
    with open(settings.user_info, 'a') as f:
        f.write('%s|%s|%s' % (msg['username'], msg['password'], pickle_path))
    return True


def upload():
    pass
