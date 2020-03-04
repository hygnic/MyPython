# User: hygnic
# Date: 2018/9/2
# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/26

user_status = False  # 用户登录了就把这个改成True
def login(func):  # 把要执行的模块从这里传进来
    def inner():
        _username = "123"  # 假装这是DB里存的用户信息
        _password = "123"  # 假装这是DB里存的用户信息
        global user_status

        if not user_status: # 现在user_status 为 False
            username = input("user: ")
            password = input("password: ")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
                print('到这里了2')   # 用于查看装饰器内部代码的执行情况
            else:
                print("wrong username or password!")

        if user_status:
            func()  # 看这里看这里，只要验证通过了，就调用相应功能
    print('到这里了1')  # 用于查看装饰器内部代码的执行情况
    return inner  # 用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数
                     # 而inner　函数返回func（）

def home():
    print('--首页--')

def america():
    print('--美国--')

def japan():
    print('--日本--')

def photo():
    print('--照片--')




# 添加方法二：
# @login
def photo():
    print('--照片--')

# 添加方法一：
photo = login(photo)



home()
japan()
