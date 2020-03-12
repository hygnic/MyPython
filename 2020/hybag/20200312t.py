# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/12

import os

# path = ur"G:\高标准分布图\崇州\510000高标准农田建设上图入库数据20200112\510000GT2012510184成都市崇州市怀远镇富丽村、黄鹤村、达通村改造完善建设高标准基本农田项目YS\GBZ2012510184GT成都市崇州市怀远镇富丽村、黄鹤村、达通村改造完善建设高标准基本农田项目YS.shp"
# a = os.path.getsize(path)
# print a

__getall_items = []
def hybag_getall_item(dirs_p, suffix, matchword=None):
	"""
	import os
	遍历获得一个文件夹（包含子文件夹）下所有的符合后缀的item
	recur 使用递归，特别注意，层数不要太多
	:param dirs_p: dir address
	:param suffix: 后缀
	:param matchword: 匹配字段，简单筛选出符合匹配字段的项目
	:return: list
	"""
	global __getall_items
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p,file_p)
		if os.path.isdir(file_path):
			# 递归
			hybag_getall_item(file_path, suffix, matchword)
		else:
			# 保证不使用matchword匹配字段时也能正常运行
			if matchword:
				# 注意matchword是 str 还是 Unicode
				if file_p[-3:].lower() == suffix and matchword in file_p and os.path.getsize(file_path)==100:
					__getall_items.append(file_path)
			else: # 没有使用匹配功能
				if file_p[-3:].lower() == suffix:
					__getall_items.append(file_path)
	return __getall_items

kkkk = hybag_getall_item(
ur"G:\高标准分布图\崇州\510000高标准农田建设上图入库数据20200112","shp","GBZ"
)

for kk in kkkk:
	print os.path.basename(kk)