# -*- coding:cp936 -*-
# User: hygnic 'liaochen'
# Date: 2019/9/17

import os, re

photos = []


def func(dirpath):
	"""��ѡ�е�Ŀ¼�µ�����Ŀ¼���ļ�����ӡ����"""
	filenames = os.listdir(dirpath)
	for filename in filenames:
		file_p = os.path.join(dirpath, filename)
		if os.path.isdir(file_p):
			# print filename
			func(file_p)
		else:  # ��ӡ��Ŀ¼���ļ�
			global photos
			# print filename
			
			photos.append(filename)
			# filename = filename.split("-")
			# s = "".join(filename)
			
			
			txt_path = r"G:\1204\1.txt"
			txt_file = file(txt_path, "r")
			text_lists = txt_file.readlines()
			
			
			ii = filename.split("-")
			ii = "".join(ii)
			for text_list in text_lists:
				# print pre_group_value[:-6],"--",text_list.strip()[:-12].decode('utf8')
				if ii[:-6] == text_list.strip()[:-12].decode('utf8'):
					new = "gst"
					pp = text_list.strip()[-12:]
					jpg = "001.jpg"
					abp = filenames
					# path1 = os.path.abspath(abp)
					# a = os.path.join(abp,i)
					# b =os.path.join(abp,new+pp+jpg)
					# print dirpath # G:\1204\��ʾ��Ƭ\л��������������
					p1 = os.path.dirname(dirpath) # G:\1204\��ʾ��Ƭ
					p_p  = os.path.join(dirpath,filename)
					new = os.path.join(dirpath,new+pp+jpg)
					print p_p
					print """ppppppp"""
					print new
					
					
					os.rename(p_p,new)
					
# func(ur"G:\1204\��ʾ��Ƭ")

def GST_rename(txt_path, jpg_path):
	"""
	�����������Ĺ�ʾͼ�����޸ĳɹ淶������
	֧��cp936(GBK)��utf8�ı����ı��Ķ���
	"""
	txt_file = file(txt_path, "r")
	text_lists = txt_file.readlines()
	jpg_lists = os.listdir(jpg_path)
	for jpg in jpg_lists:
		# ֻ��ͼƬͨ��
		if jpg.endswith('jpg'):
			for text in text_lists:
				# txt�ı�-utf8����
				try:
					text_field = text[12:].strip().decode('utf8')
					jpg_field = re.findall('\D+', jpg)[1][:-4]
				except UnicodeDecodeError:
					text_field = text[12:].strip().decode('cp936')
				finally:
					
					if text_field == jpg_field:
						oldname = os.path.join(jpg_path, jpg)
						XJQYDM = text[:12]
						newname1 = 'GST'
						newname2 = '08001.jpg'
						GSTname = newname1 + XJQYDM + newname2
						newfile = os.path.join(jpg_path, GSTname)
						showed_msg = jpg_field + " -> " + GSTname
						print showed_msg
						os.rename(oldname, newfile)
						print "Done!"


# # ������ǰ��510304107218ţ����ɽ��
# path1 = ur'E:\move on move on\df\gst.txt'
# # ͼƬ��ַ
# path2 = ur'E:\move on move on\df'
# GST_rename(path1, path2)