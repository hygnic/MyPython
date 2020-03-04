# User: hygnic
# Date: 2018/8/28

# 斐波拉切数列
# 0 1 1 2 3 5 8 13 21 34 55

# 使用递归函数
def fibo(n):
    if n == 0 or n == 1:
        return n
    return (fibo(n-1) + fibo(n-2))

print(fibo(19))
print('-----')


def outer(): #一个装饰器
    x = 10
    def inner():
        print(x)
    return inner

outer()()

f = outer()
f()

# def op():
#     c = 7
# op()
# print(c)