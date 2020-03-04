# -*- coding: cp936 -*-
# GB2312
# 2020 0111 �γ���lcc
# python2.7 arcgis10.1
"""
���ܽ��ܣ�
    ����ͳ�Ƴ��߱�׼ũ��ľ��������Ŀ����ë�����Ķ��
    �Զ���������ͼ��DIKUAIAREA�ֶε�����ֵ����Ҫ����ǰ�����ֶΣ�

"""
import arcpy


def update_layer():
    mxd1 = arcpy.mapping.MapDocument("CURRENT")
    layer1 = arcpy.mapping.ListLayers(mxd1)[0]
    layer2 = arcpy.mapping.ListLayers(mxd1)[1]
    # for layerr in [layer1,layer2]:
    #     arcpy.AddField_management(in_table=layerr,
    #                               field_name="DIKUAIAREA",
    #                               field_type="DOUBLE")
    # cursor = arcpy.da.UpdateCursor(layer1,("TBDLMJ",))
    net_area = 0
    with arcpy.da.UpdateCursor(layer1,("TBDLMJ","DIKUAIAREA")) as cursor:
        for row in cursor:
            tbdlmj = float(row[0])
            row[1] = round(tbdlmj*0.0015,4)
            cursor.updateRow(row)
            net_area +=tbdlmj
            
    area1 = 0
    with arcpy.da.UpdateCursor(layer2,("SHAPE@AREA","DIKUAIAREA")) as cursor1:
        for row in cursor1:
            gross_area = float(row[0])
            # print gross_area
            row[1] = round(gross_area * 0.0015,4)
            cursor1.updateRow(row)
            area1 += gross_area
    
    net_area = net_area*0.0015
    area1 = area1*0.0015
    print u'������Ա�\n'
    print u"���ɸ߱�׼ũ�ﾻ���: {0}Ķ".format(net_area)
    print u"��Ŀ��ë���: {0}Ķ".format(area1)

if __name__ == '__main__':
    update_layer()
