# coding:utf8
# User: hygnic
# Date: 2018/9/14
# 编码的本质就是把我们的能看懂的语言转换为机器能识别的语言
# 从utf-8转GBK：
    # 1.decode('utf8') 转为unicode
    # 2.encode（'gbk'）编码后是以我们选择的方法（比如'utf-8','gbk'）编码的byte码
        # 字节有很多种类，根据不同的编码方式有不同种类的字节
# 存储的编码和解释器编码类型是两回事，如果存储到磁盘上的编码格式和解释器默认编码格式不一致时
    # ，会出现乱码。
# 明文在保存到磁盘时一般是用unicode保存
# cmd默认的编码方式是gbk
# cpu的执行编码方式是unicode，因为它要处理所有语言
    # 解释器将数据传给cpu时，会转成unicode







# https://www.cnblogs.com/yuanchenqi/articles/5938733.html

"""
# py2 环境下
f = open('txt', 'rb')
print((f.read()))   # result： b'\xe8\x80\x81\xe5\xad\x90\xe6\x9c\x80\xe6\xa3\x92'

# f = open('txt', 'r')
# print((f.read()))  没有# coding:utf8 会出错， 和print有关好像

f = open('txt', 'r', encoding='utf-8')
print((f.read())) # result: 老子最棒
a = '集卡'
print(len(a))
"""

"""
# py2 
# 解释器默认使用ASCII编码方式，添加#coding:utf8可让其默认编码方式改为utf8






# py2中有两种数据类型，如下：

s = '集卡hi'  # 实际上数据类型是 Bytes
print len(s)  # result: 8  结果是8个，存的是字节，一个汉字占3个字节
print repr(s)  # result: \xe9\x9b\x86\xe5\x8d\xa1hi 8个字节
print type(s) # result: <type 'str'> 这个仅仅是python2.7取得名字
print s  # py2中print中自带str方法，它会将bytes字节存储的‘集卡’转换为Unicode，而unicode能对应上中文


s = u'集卡hi'      # 数据类型是 Unicode
print len(s)    # result: 4
print repr(s)   # result: u'\u96c6\u5361hi' # 存储的Unicode编码
print type(s)   # result: <type 'unicode'>


print 'a' + u'b' # result: ab, ASCII码中存在的字符可以由py2.7从bytes转换为unicode
# print  '人' + u' 看' # result：报错。 中文不在ASCII码中，所以报错
"""




# py3中
    # 两种数据类型为byte和unicode, 文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示
    # 字符拼接不能自动转数据类型了
