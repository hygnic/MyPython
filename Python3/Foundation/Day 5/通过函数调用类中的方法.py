# User: hygnic
# Date: 2018/9/6

class Wechat:
    def pay(self, money):
        print('你已经支付%s元' % money)
        return 1


we = Wechat()
print(we.pay(200))

print("=" * 20)


def pay(pay_obj, money):  # 这里的函数名必须是调用的类里有的方法
    pay_obj.pay(money)


pay(we, 300)    # pay_obj 调用了类Wechat
