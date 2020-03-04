# User: hygnic
# Date: 2018/9/18

# 先看一下属性：__dict__ （每个对象均具备该属性）
#
# 作用：字典类型，存放本对象的属性，key(键)即为属性名，value(值)即为属性的值，
#     形式为{attr_key : attr_value}
#
# 对象属性的访问顺序：
#     ①.实例属性
#     ②.类属性
#     ③.父类属性
#     ④.__getattr__()方法


class Foo():
    class_num = 10

    def __init__(self):
        self.func_num = 20

class Test():
    dd = Foo()
aa = Test()

if __name__ == '__main__':
    print(Foo())
    print(aa.dd)
    f = Foo()
    Foo.class_num = 300
    f.class_num = 200
    print('类的属性:', Foo.__dict__)  # f = Foo
    print('*' * 20)  # print('类的的属性:',f.__dict__)
    print('实例的属性:', f.__dict__)  # 输出的是类的属性，因为没有实例化（）

"""
# 结论 ：
    类的属性和实例的属性是不一样的，在类中添加的属性只有类有，比如class_num，
        如果修改会覆盖.
    。
    实例的属性在__init__中，修改不会覆盖，只会增加
    
    
    result：
        类的属性: {'__module__': '__main__', 'class_num': 300,
        '__init__': <function Foo.__init__ at 0x03309810>, 
         'test': <function Foo.test at 0x03309930>, '__dict__': <attribute '__dict__' of 'Foo' objects>, 
         '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None}
         
        ********************
        
        实例的属性: {'func_num': 20, 'class_num': 200}
   """




