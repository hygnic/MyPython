# User: hygnic
# Date: 2018/9/11
from core.auth_client import Auth


def main():
    auth_obj = None
    # 将登录和注册功能放到了core.auth_client中
    start_1 = [('登录', 'login'), ('注册', 'register'), ('退出', 'exit')]  # tuple
    for index, value in enumerate(start_1, 1):  # 参数指定索引起始值
        print(index, value[0])  # why 0?
    while True:
        try:
            num = int(input('>>>'))
            func_str = start_1[num - 1][1]  # why 0? is it related to tuple?
            print(func_str)
        except:
            pass
        # 兼顾登录方法和注册方法
        if hasattr(Auth, func_str):  # 查看是否有func_str方法
            auth_obj = Auth()
            func = getattr(auth_obj, func_str)  # 获取该方法
            ret = func()
            print('1')
            if ret: break  # 登录成功，脱离登录循环
        elif auth_obj:  # 要是有sk连接
            auth_obj.socket.sk.close()
            print('2')
            exit()
        else: # 没有对应方法，即为3对应的退出
            exit()


print('i\'m client')
