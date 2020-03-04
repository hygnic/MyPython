# User: hygnic
# Date: 2018/9/4


"""
class BAR():
    def __init__(self, a):
        self.name = a
    def koo(self):
        return 234


a = BAR(2)
print(a.koo())
print(a.name)

print('-------------------------------')

class BAR():
    def __init__(self):
        self.name = 'a'
    def koo(self):
        return 234

a = BAR()
print(a.koo())
print(a.name)


print('---------------------------------')
"""

"""
class Me():
    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.__gender = g

    def show_gender(self):
        return self.__gender


meth = Me('hygnic', 18, 'male')
# print(meth.__gender)
gend = meth.show_gender()
print(gend)

"""
"""
class YU:
    def __call__(self, *args, **kwargs):
        return 123

print(YU())

s = str(123)
print(s, type(s))

"""

class Aoo:
    """
    TEXT
    """
    def __init__(self, n):
        self.name = n

    def loo(self):
        return 3

a = Aoo('lcc')
print(a.__dict__)
print(Aoo.__dict__)

#反射（通过字符串的形式操作对象的成员）

# inp = input('>>>')  # inp实际上是字符串，然而 对象.'字符串' 是无法获取其中信息的
# v = getattr(a, inp)  # 所以需要该函数
# print(v)    # 输入name可以获取对象中的name信息

v = getattr(a, 'loo') # 第二个参数必须是字符串才行
print(v())

# hasattr() 该方法用于查看类中是否有那些字段，参数二应该是字符串
# setattr() 添加值，存储于对象的内存中
# delattr() 删除用