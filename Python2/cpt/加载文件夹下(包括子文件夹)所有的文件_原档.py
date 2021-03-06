# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/11
# Python2 arcgis10.6
import arcpy,os

def hybag_addshp(shp_path,df_name=None,fresh=True):
	"""
	import arcpy,os
	加载shp文件到当前mxd
	:param shp_path: file path.
	:param df_name: dataframe name; default first df.
	:param fresh:bollean; refresh; default ture.
	:return: None
	"""
	mxd = arcpy.mapping.MapDocument("CURRENT")
	dataframe = arcpy.mapping.ListDataFrames(mxd,df_name)[0]
	layer = arcpy.mapping.Layer(shp_path)
	arcpy.mapping.AddLayer(dataframe, layer, "AUTO_ARRANGE")
	if fresh:
		arcpy.RefreshActiveView()  # 刷新地图和布局窗口
		arcpy.RefreshTOC()  # 刷新内容列表

_getall_items = []
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
	global _getall_items
	for file_p in os.listdir(dirs_p):
		file_path = os.path.join(dirs_p,file_p)
		if os.path.isdir(file_path):
			# 递归
			hybag_getall_item(file_path, suffix, matchword)
		else:
			# arcpy.AddMessage(4)
			if matchword: # 保证不使用matchword匹配字段时也能正常运行
				# arcpy.AddMessage(6)
				if file_p[-3:].lower() == suffix and matchword in file_p:
					print type(matchword)
					__getall_items.append(file_path)
			else:
				# arcpy.AddMessage(9)
				if file_p[-3:].lower() == suffix:
					print type(matchword)
					__getall_items.append(file_path)
	return __getall_items


dir_path = arcpy.GetParameterAsText(0)
match_w = arcpy.GetParameterAsText(1)
arcpy.AddMessage(match_w)
arcpy.AddMessage(type(match_w))

match_w = str(match_w)
print match_w
print type(match_w)
arcpy.AddMessage(match_w)
arcpy.AddMessage(type(match_w))

filelist = hybag_getall_item(dir_path,"shp",matchword=match_w)
count = len(filelist)
arcpy.AddMessage("\n"+"loading...")
for afile in filelist:
	hybag_addshp(afile)
msg1 = str(count)+ " files loaded"
arcpy.AddMessage("\n"+msg1)


# if __name__ == '__main__':
# 	files = hybag_getall_item(
# 		ur"G:\高标准分布图\青川县\510000高标准农田建设上图入库数据20200113","shp","GBZ")
# 	print len(files)
# 	for afile in files:
# 		hybag_addshp(afile)
# 	msg1 = u"{0}个文件加载完成".format(len(files))
# 	print msg1
# #
			
		
		