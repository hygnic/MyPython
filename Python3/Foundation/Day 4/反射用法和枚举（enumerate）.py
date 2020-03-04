# User: hygnic
# Date: 2018/9/19
func_list = [(': 添加', 'add'),(': 修改', 'alter'),(': 删除', 'delete')]
class SomeFunction():

    def add(self):
        print('add Done！')

    def alter(self):
        print('alter Done！')

    def delete(self):
        print('delete Done！')


for index,first_value in enumerate(func_list,1):
    print(index,first_value[0]) # print(index,first_value) # 效果些许不一样
while True:
    # try:
        select_num = input('input number of the function which you want!\n >>>')
        select_num = int(select_num) - 1
        func_str = func_list[select_num][1]
        sf = SomeFunction()  # getattr 反射的对象得是实例，所以将类实例化了
        func = getattr(sf, func_str)
        func()

    # except: # 用来避免数字超过3
    #     print('please input number again!')
    #     continue

