# -*- coding:cp936 -*-
import arcpy,os

# ��Ҫ��ͼmxd�ĵ��ļ�Ŀ¼
path1 = raw_input('�����ͼ�ĵ�Ŀ¼��')
# path1 = r'G:\������'
path2 = r'G:\��ʾͼ��ͼ2019\������\�ɹ�OKOK\2\ͼƬ'

# Դ���ݿ�Ŀ¼
path3 = r'G:\��ʾͼ��ͼ2019\������\��ͼ2.gdb'

# ���÷ֱ���
res = raw_input('���÷ֱ��ʣ�')
res = int(res)

# ���Խ��и���
arcpy.env.overwriteOutput = True

for afile in os.listdir(path1):
    if afile[-3:].lower() == 'mxd':
        print "\n�����ȷ"
        mxd1 = arcpy.mapping.MapDocument(os.path.join(path1,afile))
        
        # �����޸�����
        
        #for lyr1 in arcpy.mapping.ListLayers(mxd1):
           # if lyr1.isBroken == True:
            #    lyr1.findAndReplaceWorkspacePath('',path3)
               
            # houzui = afile[-3].lower() + "jpg"
        #print '�����޸����\n'
        #mxd1.save()
        print '��ʼ��ͼ'
        # ExportToJEPG�ĵڶ��������ǵ���ͼƬ�����ƺ�Ŀ¼����
        arcpy.mapping.ExportToJPEG(mxd1,os.path.join(path1,afile[:-3] + 'jpg'),resolution = res) 
        print afile + ' ��ͼ���'
        
        del mxd1
    else:
        print '\n�ǵ�ͼ�ĵ�������'
