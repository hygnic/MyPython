# -*- coding: utf-8 -*-
# User: hygnic
# Date: 2019/10/4

import hashlib

def md5(pwd):
	# 使用md5算法，jiayan 加盐
	obj = hashlib.md5(b'jiayan')
	# 写入要加密的字节
	obj.update(pwd.encode('utf8'))
	# 获取密文
	a = pwd.encode('utf8')
	return obj.hexdigest(),a

print(md5('ioio'))
