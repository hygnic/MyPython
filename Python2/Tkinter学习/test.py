# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 201# -*- coding: utf-8 -*-
# # User: liaochenchen, hygni c
# # Date: 2019/11/15
#
# D:\Program Files\ArcGIS\Python27\ArcGIS10.4\tcl\tcl8.5
# TCL_LIBRARY
import sys
sys.path.append(r"D:\Program Files\Python3.74\tcl\tcl8.6")


import PySimpleGUI as sg
sg.change_look_and_feel('DarkAmber')   # Add a little color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()