# User: hygnic
# Date: 2018/9/19

def register():
    # 输入用户名，pw
    # 判断用户是否存在
    # 将数据插入到userinfo表中
    pass


def login():
    while True:
        username = input('输入用户名')
        password = input('输入密码')
        pwd =commons.md5(password)
        user_repository = UserInfoRepository()
        user_info = user_repository.fetch_by_user_pwd(username,pwd)
        if not user_info:
            print('错误，重新输入')
            continue


def execute():
    while True:
        print('欢迎使用登录系统：1：登录；2：注册；3：找回密码；\n')
        dic = {
            '1': login,
            '2': register,
            '3': find_pwd
        }
        choice = input('请输入选项')
        if choice not in dic.keys():
            print('输入错误')
            continue
        func = dic[choice]
        result = func()
        if result:
            choice_menu()

