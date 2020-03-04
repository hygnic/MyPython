# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/24

# User: hygnic
# Date: 2018/9/19
func_list = [(u': 添加', 'add'),(u': 修改', 'alter'),(u': 删除', 'delete')]
class SomeFunction(object):

    def add(self):
        print 'add Done!'
    def alter(self):
        print 'alter Done!'
    def delete(self):
        print 'delete Done!'
v = getattr(SomeFunction,"add")
v()
for index,first_value in enumerate(func_list,1):  # 索引从1开始
    print index,first_value[0] # print(index,first_value) # 效果些许不一样
while True:
    # try:
        select_num = input('input number of the function which you want!\n >>>')
        select_num = int(select_num) - 1
        func_str = func_list[select_num][1]
        sf = SomeFunction()  # getattr 反射的对象得是实例，所以将类实例化了
        func = getattr(sf, func_str) # 从对象中寻找func_str方法
        func() # 执行该方法

    # except: # 用来避免数字超过3
    #     print('please input number again!')
    #     continue