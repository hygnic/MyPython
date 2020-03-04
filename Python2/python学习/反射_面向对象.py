# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/24
# class UserLogin(object):
# 	def login(self):
# 		print "login"
#
# 	def register(self):
# 		print "register"
#
# 	def logout(self):
# 		print "logout"
#
# 	def run(self):
# 		command_line = [
# 			"login",
# 			"register",
# 			"logout"
# 		]
# 		# c= [commd+"\n"  for commd in command_line]
# 		f_str = raw_input(command_line)
# 		# 第一种调用方式
# 		func = getattr(self, f_str)
# 		func()
# 		# 第二种调用方式
# 		# func = getattr(UserLogin,f_str)
# 		# func(self)
#
#
# obj = UserLogin()
# obj.run()

class UserLogin(object):
	def __init__(self):
		self.a = None
	def run(self):
		print self.a
		
obj = UserLogin()
setattr(obj,"a",2)
obj.run()
