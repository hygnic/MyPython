# User: hygnic
# Date: 2018/9/14
import json
"""
# py3

s = '集卡'
b1 = s.encode('utf-8')
print(b1, type(b1))

print(b1.decode('utf-8'))
print(type(b1.decode('utf-8'))) # <class 'str'> str表示，实际是unicode
print(json.dumps(s))  # result: "\u96c6\u5361"    所以上一句话是对的，本质是unicode
print(b1.decode('gbk')) # 乱码，没用相对应的编码方法解码

print('*'*10)
d = '哦哦'
b=bytes(d, 'utf8')
print(b)

# 解码方法一
# dd = b.decode('utf8')
# print(dd)

# 解码方法二 使用str方法
dd = str(b, 'utf8')
print(dd)

"""