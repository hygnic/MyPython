# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/23
import os
def func(dirpath):
	"""将选中的目录下的所有目录和文件都打印出来"""
	filenames = os.listdir(dirpath)
	for filename in filenames:
		file_p = os.path.join(dirpath, filename)
		if os.path.isdir(file_p):
			print filename
			func(file_p)
		else: # 打印非目录的文件
			print filename
func(r"E:\move on move on\Python2\gisTK")

# bin
# shell
# entrance.py
# docs
# GiSpot
# Map
# ejpg.py
# export_jpeg.pyc
# Icons
# test
# tooltk.py
# GUIs
# help.py
# tooltk.py
# tooltk.pyc


# 改进版本，能区分目录的相互关系
def func2(dirpath, counter):
	"""将选中的目录下的所有目录和文件都打印出来"""
	filenames = os.listdir(dirpath)
	for filename in filenames:
		file_p = os.path.join(dirpath, filename)
		if os.path.isdir(file_p):
			print "\t"*counter,filename
			func2(file_p, counter+1)
		else: # 打印非目录的文件
			print "\t"*counter,filename
func2(r"E:\move on move on\Python2\gisTK",0)

# bin
# 	shell
# 		entrance.py
#  docs
#  GiSpot
# 	Map
# 		ejpg.py
# 		export_jpeg.pyc
# 	Icons
# 	test
# 		tooltk.py
#  GUIs
# 	help.py
# 	tooltk.py
# 	tooltk.pyc

lst = [0,2,2,3]
lst[2]

