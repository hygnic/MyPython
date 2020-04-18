# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/25
# python2.7  numpy (1.9.3)

import arcpy
import numpy

out_fc = ur'G:\1204\tr'

# Create a numpy array with an id field, and a field with a tuple
#  of x,y coordinates
arr = numpy.array([(1, (471316.3835861763, 5000448.782036674)),
                   (2, (470402.49348005146, 5000049.216449278))],
                  numpy.dtype([('idfield', numpy.int32),('XY', '<f8', 2)]))

# Define a spatial reference for the output feature class
spatial_ref = arcpy.Describe(ur"G:\内江市\市中区分布图\出图2.gdb\出图范围").spatialReference

# Export the numpy array to a feature class using the XY field to
#  represent the output point feature
arcpy.da.NumPyArrayToFeatureClass(arr, out_fc, ['XY'], spatial_ref)

