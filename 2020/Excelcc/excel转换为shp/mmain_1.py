# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2020/2/19
# arcgis 10.6  pandas

import arcpy,os

workspace = r"G:\works"
excel_file = ur"G:\蓬溪\蓬溪县明月镇桂花桥村、广坝村、九块田村、宇安村、龙拱背村、火石村、碧山庙村、白庙村土地整理项目11\蓬溪县明月镇桂花桥村、广坝村、九块田村、宇安村、龙拱背村、火石村、碧山庙村、白庙村土地整理项目.xlsx"
excel_file2 = ur"G:\蓬溪\23.txt"
print os.path.isfile(excel_file)

arcpy.env.workspace = workspace
print "ok"
arcpy.ExcelToTable_conversion(excel_file,"we")