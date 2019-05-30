# -*- coding:utf8 -*-
# @TIME     :2019/5/30 16:12
# @Author   : 洪松
# @File     : test1.py

import numpy as np
'''
np.sort返回的是数组的已排序副本
而就地排序则会修改数组本身
'''
arr = np.random.randn(8)
print('arr: ', arr, sep='\n')
arr.sort()
print('arr_sorted: ', arr, sep='\n')


arr_1 = np.random.randn(5, 3)
print('arr_1: ', arr_1, sep='\n')
# arr_1.sort(1)# 1 按行排序； 0 按列排序
# print('arr_1_sorted_row: ', arr_1, sep='\n')
arr_1.sort(0)
print('arr_1_sorted_col: ', arr_1, sep='\n')


