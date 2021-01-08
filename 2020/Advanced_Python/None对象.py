#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/1/8 12:49
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
blank_list =[]
"""1
__________________________________________________________________________"""
if blank_list:
    print("ok") # 无输出

if blank_list is not None:
    print("ok2") # 输出 ok2

"""2 类的内部实现
__________________________________________________________________________"""

class TestNoneType:
    def __init__(self):
        pass
    
    def __len__(self):
        print("ok")
        return False

testinstance = TestNoneType()
if testinstance:
    print(2)