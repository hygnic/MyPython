# User: hygnic
# Date: 2018/9/12
import os
from config import settings


class User:
    def __init__(self, name):
        self.name = name
        self.home = os.path.join(settings.home_path,
                                 name)  # 根据不同用户创建各自的用户文件夹的地址（在家目录下）
        self.cur_path = self.home
        self.disk_space = settings.space
        self.file_size = 0
