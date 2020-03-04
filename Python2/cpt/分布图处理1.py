# -*- coding: cp936 -*-
# 2019 08 15 �γ���


import arcpy
import datetime
import os

time1 = datetime.datetime.now()
time2 = datetime.datetime.strptime("2020-1-1", "%Y-%impure_data-%d")
if time1 > time2:
	arcpy.AddError(u'\n\n�����𻵣�����ϵ�γ���\n\n')
else:
	# ģ��Ŀ¼��ֻ��Ҫһ�����ú��˵�mxd�ļ�
	# template = 'G:/������/�����߷ֲ�ͼ0815/��������ļ�/������.mxd'
	template = 'CURRENT'
	# template = template.decode('utf-8')
	
	
	# �������Ŀ¼
	outputclass = arcpy.GetParameterAsText(0)
	# outputclass = u'G:/�Ͻ���/�Ͻ��ֲ�ͼ/�����ͼ�ĵ�'
	# outputclass = outputclass.decode('utf-8')
	# outputclass = outputclass.decode('gb2312')
	
	# ���û������ļ����Ŀ¼
	bufferoutclass = arcpy.GetParameterAsText(1)
	# bufferoutclass = u'G:/�Ͻ���/�Ͻ��ֲ�ͼ/�������ļ�'
	# bufferoutclass = bufferoutclass.decode('gb2312')
	
	# ���Խ��и���
	arcpy.env.overwriteOutput = True
	
	# ��ȡ�ļ�
	mxd1 = arcpy.mapping.MapDocument(template)
	print mxd1.title
	dataframe1 = arcpy.mapping.ListDataFrames(mxd1)[0]
	dataframe2 = arcpy.mapping.ListDataFrames(mxd1)[1]
	
	# ���뽫��һ��ͼ������Ϊ����ͼ�㣬�����˳�����
	if not mxd1.activeDataFrame == dataframe1:
		arcpy.AddError(u'\n\n�뼤���һ�����ݿ򣡣�����\n\n')
	else:
		# �������ݿ�����XJQY�ĸ�������������Ϊ�������Ľ�����׼��
		tempDB = u'�м䴦���ݴ����ݿ�.gdb'
		arcpy.CreateFileGDB_management(bufferoutclass, tempDB)
		
		print dataframe1.name + u'ͼ���ȡ�ɹ�'
		print dataframe2.name + u'ͼ���ȡ�ɹ�'
		
		# ƥ���ֶ���CJQYDM
		layerlist1 = ['��־��', '����']
		
		# ƥ���ֶ���XJQYDM
		layerlist2 = ['XJQY', '����פ��', '��ί��', 'DZDW', 'XZDW', '���']
		
		# �Ӹ�ͼ���ж�ȡ���Ա���Ϣ����������������ͼ��
		datalayer = arcpy.mapping.ListLayers(mxd1, 'XJQY', dataframe1)[0]
		datalayer.definitionQuery = ""
		cursor = arcpy.da.SearchCursor(datalayer, ('XJQYDM', 'XJQYMC', 'XJXZQ'))
		namelist = []
		arcpy.AddMessage('��������ѯ...')
		# ��ȡXJQYDM
		for row in cursor:
			getvalue_XJQYDM = row[0]
			getvalue_XJQYMC = row[1]
			getvalue_MC = row[2]
			# �����ѯ
			# '��־��','����'
			for onelayerlist in layerlist1:
				layer = arcpy.mapping.ListLayers(mxd1, onelayerlist, dataframe1)[0]
				# ��ʱ���־����ʱû��
				if not layer.isBroken:
					layer.definitionQuery = '"' + 'CJQYDM' + '"' + ' like' \
											+ " '" + getvalue_XJQYDM[:9] + "%'"
				
				# 'XJQY','����פ��','��ί��','DZDW','XZDW','���'
			for onelayerlist in layerlist2:
				layer = arcpy.mapping.ListLayers(mxd1, onelayerlist, dataframe1)[0]
				# layer.definitionQuery = ''
				layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
				
				# ����Ƭ�鼰��������
			layer = arcpy.mapping.ListLayers(mxd1, '����Ƭ�鼰��������', dataframe1)[0]
			layer.definitionQuery = '"' + 'LQPKDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM + "%'"
			
			# LQDK�ں�
			layer = arcpy.mapping.ListLayers(mxd1, 'LQDK�ں�', dataframe1)[0]
			layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
			
			# DLTB�ں�_·��_�����ͼ
			layer = arcpy.mapping.ListLayers(mxd1, 'DLTB�ں�_·��_�����ͼ', dataframe1)[0]
			layer.definitionQuery = '"' + 'QSDWDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM + "%'"
			
			# DLTB�ں�
			layer = arcpy.mapping.ListLayers(mxd1, 'DLTB�ں�', dataframe1)[0]
			layer.definitionQuery = '"' + 'QSDWDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM + "%'"
			
			# �޸ĵڶ���ͼ��Ķ����ѯ
			layer = arcpy.mapping.ListLayers(mxd1, 'XJQY', dataframe2)[0]
			layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
			
			# ���õ�ͼ�ĵ��е�����Ԫ��
			for elm in arcpy.mapping.ListLayoutElements(mxd1, 'TEXT_ELEMENT'):
				if elm.name == 'BT1':
					elm.text = u'%s%s"����"ũ��ռ�ֲ�ͼ' % (getvalue_MC, getvalue_XJQYMC)
				if elm.name == 'BT2':
					elm.text = u'%s��%s��λ��ʾ��ͼ' % (getvalue_XJQYMC, getvalue_MC)
			
			# ���ŵ����ߴ�
			layer = arcpy.mapping.ListLayers(mxd1, 'XJQY', dataframe1)[0]
			dataframe1.extent = layer.getSelectedExtent()
			dataframe1.scale = 10000
			
			arcpy.env.workspace = bufferoutclass
			# ��ѡ������ݵ�������ݿ���
			arcpy.FeatureClassToGeodatabase_conversion(datalayer,
													   bufferoutclass + '/' + tempDB)
			# �����ݿ����ļ�������
			prename = bufferoutclass + '/' + tempDB + '/' + 'GPL0'
			# prename = bufferoutclass + '/' + tempDB + '/' + 'XJQY'
			
			# arcpy.AddMessage(os.listdir(bufferoutclass + '/' + tempDB))
			
			arcpy.Rename_management(prename, getvalue_XJQYMC)
			
			namelist.append(getvalue_XJQYMC)
			# ����ͼ�ĵ�
			mxd1.saveACopy(outputclass + '/' + getvalue_XJQYMC + '.mxd')
		del cursor
		
		# �����б�
		namelist.sort()
		
		arcpy.env.workspace = bufferoutclass
		arcpy.AddMessage('���û�����...')
		
		for aname in namelist:
			# ���ɻ�����
			inFeatures = tempDB + '/' + aname
			outFeatureClass = bufferoutclass + '/' + aname
			distance = [30, 60, 90]
			bufferunit = 'meters'
			arcpy.MultipleRingBuffer_analysis(inFeatures, outFeatureClass, distance,
											  bufferunit, '', '', 'OUTSIDE_ONLY')
			
			dellayer = arcpy.mapping.ListLayers(mxd1, '', dataframe1)[0]
			if not dellayer.name == 'XJQY':
				arcpy.mapping.RemoveLayer(dataframe1, dellayer)
			print 'buffer complete!'
		
		# �øո����ɵĻ��λ������ļ��滻������mxd�е�'������'ͼ��
		# ��ȡ���ɵĵ�ͼ�ĵ�
		
		# import arcpy,os
		# outputclass = u'G:\\�Ͻ���\\�Ͻ��ֲ�ͼ\\�����ͼ�ĵ�'
		# bufferoutclass = u'G:\\�Ͻ���\\�Ͻ��ֲ�ͼ\\�������ļ�'
		# tempDB = u'�м䴦���ݴ����ݿ�.gdb'
		for newfile in os.listdir(outputclass):
			if newfile[-3:].lower() == 'mxd':
				# ������ѡ����
				xxxx = newfile[:-4]
				# �������ǽ����ؼ����mxd����mxdĿ¼�������Ҳ�����Ӧ������������
				if xxxx in namelist:
					newMXD = arcpy.mapping.MapDocument(os.path.join(outputclass, newfile))
					# versionpath = outputclass+'/'+version
					newlayer = arcpy.mapping.ListLayers(newMXD, '������')[0]
					# ����mxd�ĵ�������ͬ�Ļ������滻��ȥ
					newlayer.replaceDataSource(bufferoutclass, 'SHAPEFILE_WORKSPACE', xxxx)
					newMXD.save()
		
		arcpy.Delete_management(bufferoutclass + '/' + tempDB)
		arcpy.AddMessage('Done!')
