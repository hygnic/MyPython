# -*- coding:cp936 -*-
import arcpy,os

# ������Ҫ��ͼmxd�ĵ��ļ�Ŀ¼
# path1 = arcpy.GetParameterAsText(0)
path1 = ur"G:\�ڽ���\�������ֲ�ͼ\MXD"

# ���÷ֱ���
# res = arcpy.GetParameterAsText(1)
res = 300
# ���Խ��и���
arcpy.env.overwriteOutput = True

for afile in os.listdir(path1):
    if afile[-3:].lower() == 'mxd':
        mxd1 = arcpy.mapping.MapDocument(os.path.join(path1,afile))
        print "���ڳ�ͼ..."
        
        # ExportToJEPG�ĵڶ��������ǵ���ͼƬ�����ƺ�Ŀ¼����
        arcpy.mapping.ExportToJPEG(mxd1,os.path.join(path1,afile[:-3] + 'jpg'),resolution = res) 
        # arcpy.AddMessage(afile[:-4]+"�����ɹ���")
        
        del mxd1
        print afile,'Done'
    else:
        print "\n��MXD�ļ�,����"
