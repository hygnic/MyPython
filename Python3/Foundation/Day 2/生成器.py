# User: hygnic
# Date: 2018/8/28

# 生成器有两种创建方式：
# 1. s = (x for x in range(10))
# 2. yield （用于函数时，可以在断层处重新运行函数）


"""
s = (x for x in range(10))  # s = [x for x in range(10)],这个就是一个普通列表
print(s)
print('*'*20)

print(next(s))   # 等价于print(s.__next__()) 但不常用
print(next(s))
print(next(s))
print(next(s))
print(next(s))

#生成器就是一个可迭代对象（Iterable)
print('----------')
for i in s:   # 速度很快，每次检索只占用一个内存地址
    print(i)    # for方法会自动调用next()
"""



print('----------')
def yie():
    print('ok')
    count = yield 1
    print(count)
    yield 3

func = yie()
a = func.send(None) # 等于next（func） 用于进入yield函数(这里不能赋值，否则不能进入yield)之后将字符串‘abc’赋予变量‘count’
b = func.send('abc')  # 最后函数yield的值会返回到a里
print(a)
print(b)


