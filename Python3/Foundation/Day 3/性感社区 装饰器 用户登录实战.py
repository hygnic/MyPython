# User: hygnic
# Date: 2018/9/2
# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/12/26

user_status = False  # �û���¼�˾Ͱ�����ĳ�True
def login(func):  # ��Ҫִ�е�ģ������ﴫ����
    def inner():
        _username = "123"  # ��װ����DB�����û���Ϣ
        _password = "123"  # ��װ����DB�����û���Ϣ
        global user_status

        if not user_status: # ����user_status Ϊ False
            username = input("user: ")
            password = input("password: ")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
                print('��������2')   # ���ڲ鿴װ�����ڲ������ִ�����
            else:
                print("wrong username or password!")

        if user_status:
            func()  # �����￴���ֻҪ��֤ͨ���ˣ��͵�����Ӧ����
    print('��������1')  # ���ڲ鿴װ�����ڲ������ִ�����
    return inner  # �û�����loginʱ��ֻ�᷵��inner���ڴ��ַ���´��ٵ���ʱ����()�Ż�ִ��inner����
                     # ��inner����������func����

def home():
    print('--��ҳ--')

def america():
    print('--����--')

def japan():
    print('--�ձ�--')

def photo():
    print('--��Ƭ--')




# ��ӷ�������
# @login
def photo():
    print('--��Ƭ--')

# ��ӷ���һ��
photo = login(photo)



home()
japan()
