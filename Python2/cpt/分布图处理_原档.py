# -*- coding: cp936 -*-
# 2019 08 15 �γ���

import arcpy,os,sys

# ģ��Ŀ¼��ֻ��Ҫһ�����ú��˵�mxd�ļ�
# template = 'G:/������/�����߷ֲ�ͼ0815/��������ļ�/������.mxd'
template = 'CURRENT'
# template = template.decode('utf-8')

# �������Ŀ¼
outputclass = u'G:/�Ͻ���/�Ͻ��ֲ�ͼ/�����ͼ�ĵ�'
# outputclass = outputclass.decode('utf-8')
# outputclass = outputclass.decode('gb2312')

# ���û������ļ����Ŀ¼
bufferoutclass = u'G:/�Ͻ���/�Ͻ��ֲ�ͼ/�������ļ�'
# bufferoutclass = bufferoutclass.decode('gb2312')

# �������ݿ�����XJQY�ĸ�������������Ϊ�������Ľ�����׼��
tempDB = u'�м䴦���ݴ����ݿ�.gdb'
arcpy.CreateFileGDB_management(bufferoutclass,tempDB)

# ���Խ��и���
arcpy.env.overwriteOutput = True

# ��ȡ�ļ�
mxd1 = arcpy.mapping.MapDocument(template)
print mxd1.title
dataframe1 = arcpy.mapping.ListDataFrames(mxd1)[0]
dataframe2 = arcpy.mapping.ListDataFrames(mxd1)[1]

# ���뽫��һ��ͼ������Ϊ����ͼ�㣬�����˳�����
if not mxd1.activeDataFrame == 'ͼ��':
    sys.exit()
    print '����ͼ�����'
    
print dataframe1.name+ u'ͼ���ȡ�ɹ�'
print dataframe2.name+ u'ͼ���ȡ�ɹ�'



# ƥ���ֶ���CJQYDM
layerlist1 = ['��־��','����']

# ƥ���ֶ���XJQYDM
layerlist2 = ['XJQY','����פ��','��ί��','DZDW','XZDW','���']

# ƥ���ֶ���QSDWMC1


#�Ӹ�ͼ���ж�ȡ���Ա���Ϣ����������������ͼ��
datalayer = arcpy.mapping.ListLayers(mxd1,'XJQY',dataframe1)[0]


cursor = arcpy.da.SearchCursor(datalayer,('XJQYDM','XJQYMC','XJXZQ'))
namelist = []

# ��ȡXJQYDM
for row in cursor:

    getvalue_XJQYDM = row[0]
    getvalue_XJQYMC = row[1]
    getvalue_MC = row[2]
    

    # �����ѯ
        # '��־��','����'
    for onelayerlist in layerlist1:
        layer = arcpy.mapping.ListLayers(mxd1,onelayerlist,dataframe1)[0]
        # ��ʱ���־����ʱû��
        if layer.isBroken == False:
            # layer.definitionQuery = ''
            layer.definitionQuery = '"' + 'CJQYDM' + '"' + ' like' \
            + " '" + getvalue_XJQYDM[:9] + "%'"
        
        # 'XJQY','����פ��','��ί��','DZDW','XZDW','���'
    for onelayerlist in layerlist2:
        layer = arcpy.mapping.ListLayers(mxd1,onelayerlist,dataframe1)[0]
        # layer.definitionQuery = ''
        layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
        
        # XZDW
    # layer =  arcpy.mapping.ListLayers(mxd1,'XZDW',dataframe1)[0]   
    # layer.definitionQuery = '"' + 'QSDWDM1' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM +"%'"
    
    
        # ����Ƭ�鼰��������
    layer =  arcpy.mapping.ListLayers(mxd1,'����Ƭ�鼰��������',dataframe1)[0]   
    layer.definitionQuery = '"' + 'LQPKDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM +"%'"
    
        # LQDK�ں�
    layer =  arcpy.mapping.ListLayers(mxd1,'LQDK�ں�',dataframe1)[0]   
    layer.definitionQuery = '"' + 'LQDKDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM +"%'"
    
        # DLTB�ں�
    layer =  arcpy.mapping.ListLayers(mxd1,'DLTB�ں�',dataframe1)[0]   
    layer.definitionQuery = '"' + 'QSDWDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM +"%'"
        
        # �޸ĵڶ���ͼ��Ķ����ѯ
    layer = arcpy.mapping.ListLayers(mxd1,'XJQY',dataframe2)[0]
    layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
    
    # ���õ�ͼ�ĵ��е�����Ԫ��
    for elm in arcpy.mapping.ListLayoutElements(mxd1,'TEXT_ELEMENT'):
        if elm.name=='BT1':
            elm.text = u'%s%s"����"ũ��ռ�ֲ�ͼ'%(getvalue_MC,getvalue_XJQYMC)
        if elm.name=='BT2':
            elm.text = u'%s��%s��λ��ʾ��ͼ'%(getvalue_XJQYMC,getvalue_MC)


    # ����
    # ������ͼ��
    layer = arcpy.mapping.ListLayers(mxd1,'XJQY',dataframe1)[0]
    dataframe1.extent = layer.getSelectedExtent()
    dataframe2.scale = 10000

    
    arcpy.env.workspace = bufferoutclass
    # ��ѡ������ݵ�������ݿ���
    arcpy.FeatureClassToGeodatabase_conversion(datalayer,bufferoutclass + '/' + tempDB)
    # �����ݿ����ļ�������
    prename = bufferoutclass+'/'+tempDB+'/'+'GPL0'
    arcpy.Rename_management(prename,getvalue_XJQYMC)
    
    
    namelist.append(getvalue_XJQYMC)
    
    # �����ͼ�ĵ�
    mxd1.saveACopy(outputclass+'/'+getvalue_XJQYMC+'.mxd')
del cursor
print 'raw_mxd saved!'

# �����б�
namelist.sort()



arcpy.env.workspace = bufferoutclass

    
    
for aname in namelist:

   
    # ���ɻ�����
    inFeatures = tempDB + '/' + aname
    outFeatureClass = bufferoutclass + '/' + aname
    distance = [30,60,90]
    bufferunit = 'meters'
    arcpy.MultipleRingBuffer_analysis(inFeatures,outFeatureClass,distance,bufferunit,'','','OUTSIDE_ONLY')
    
    dellayer = arcpy.mapping.ListLayers(mxd1,'',dataframe1)[0]
    arcpy.mapping.RemoveLayer(dataframe1,dellayer)
print 'buffer completed!'
    
# �øո����ɵĻ��λ������ļ��滻������mxd�е�'������'ͼ��
    # ��ȡ���ɵĵ�ͼ�ĵ�
    

for newfile in os.listdir(outputclass):
    # ������ѡ����
    xxxx = newfile[:-4]
    newMXD = arcpy.mapping.MapDocument(os.path.join(outputclass,newfile))
    newlayer = arcpy.mapping.ListLayers(newMXD,'������')[0]
    # ����mxd�ĵ�������ͬ�Ļ������滻��ȥ
    newlayer.replaceDataSource(bufferoutclass,'SHAPEFILE_WORKSPACE',xxxx)
    newMXD.save()

print 'mxd saved!'

# ���������汾


    


'''
# ���ɻ�����
inFeatures = tempDB + '/' + 'GPL0'
outFeatureClass = getvalue_XJQYMC + u'���λ�����'
distance = [30,60,90]
bufferunit = 'meters'
arcpy.MultipleRingBuffer_analysis(inFeatures,outFeatureClass,distance,bufferunit,'','','OUTSIDE_ONLY')

# �滻�ļ�
    # �øո����ɵĻ��λ������ļ��滻ģ���е�'������'ͼ��
infile = outFeatureClass
datalayer1.replaceDataSource(bufferoutclass,'SHAPEFILE_WORKSPACE',infile)
print 'replace!'

# ��������������ѡͼ��
datalayer1.getExtent()
'''
# ���ɻ�����


'''
# ʹ�ø÷���ʱ�����Զ��Ƴ���ǰ��ͼ�ĵ��е�XJQY�����±���000732���ļ�ȱʧ�����ݲ��������ԭ�򣬿���������ʽ�������й�ϵ

# arcpy.env.workspace = u'G:/������/�����߷ֲ�ͼ0815/��ͼ����'

# inFeatures = u'G:/������/�����߷ֲ�ͼ0815/������/�����1.shp'
inFeatures = datalayer
# ������λ�ú����֣���������������ݿ��У���׺
    # �����'�ֲ�ͼģ��.mxd23'�Ļ����е������ߣ�����'mxd23',û�е㣬ȫ���
# ��������ĸ��Ի������ļ�����
bufName = getvalue_XJQYMC + 'buffer'
outFeatureClass = bufferoutclass + '/' + bufName

# +'/Buffer'+getvalue_XJQYMC+'.shp'
distance = [30,60,90]
bufferunit = 'meters'
# ����໷����
arcpy.MultipleRingBuffer_analysis(inFeatures,outFeatureClass,distance,bufferunit,'','','OUTSIDE_ONLY')
'''
    
    
    
    #�滻����������Դ
    
    
    
    
    
    
    
    # ��ѡȡ��ͼ�ĵ���MXDʱ('CURRENT')������Ļ����ļ�����ӵ�mxd��
        # �滻���λ������滻��ģ�建������Դ����
    # for dellayer in arcpy.mapping.ListLayers(mxd1,'������',dataframe1):
        # if dellayer.name == u'������':
        # dellayer.replaceDataSource(bufferoutclass,'SHAPEFILE_WORKSPACE',bufName)
        # print 'updata complete!'
        
        
        # else:
            # �Ƴ������ļ�ͼ��
            # arcpy.mapping.RemoveLayer(dataframe1,bufName)
            # print bufName
            # print 'del!'
            # if dellayer.name == bufName:
                # arcpy.mapping.RemoveLayer(dataframe1,dellayer)
        

    
    




# print 'ok'

# ��־20190816
    # ��ʽ��cursor����getValueһֱѭ����ȡ���ٶ��������ܲ���

        # cursor = arcpy.SearchCursor(layer)

        # for row in cursor:
            # print row.getValue('CJQYDM')
            # layer.definitionQuery = 'CJQYDM' +'=' +row.getValue('CJQYDM')[:9]



# mxd1.save()
