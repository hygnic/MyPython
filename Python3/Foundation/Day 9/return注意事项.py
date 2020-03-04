# User: hygnic
# Date: 2018/9/13

def login(user, pwd):
    if user == '123' and pwd == '123':
        return 'login successful'
    return 'login error'
    print('ok')  # return 后的函数不会执行


user, pwd = input('user: ').strip(), input('pwd: ').strip()
print(login(user, pwd))
