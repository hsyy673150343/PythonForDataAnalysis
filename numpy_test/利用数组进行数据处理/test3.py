# -*- coding:utf8 -*-
# @TIME     :2019/5/30 15:56
# @Author   : 洪松
# @File     : test3.py

import numpy as np
'''数学和统计方法'''

arr = np.random.randn(5, 4)
print('arr: ', arr, sep='\n')

'''
求均值
经常操作的参数为axis，以m * n矩阵举例：

axis 不设置值，对 m*n 个数求均值，返回一个实数

axis = 0：压缩列，对各列求均值，返回 1* n 矩阵

axis = 1 ：压缩行，对各行求均值，返回 m *1 矩阵
'''
print('arr_mean: ', arr.mean(), sep='\n')
print('arr_mean: ', np.mean(arr), sep='\n')
print('arr_mean_col: ', arr.mean(axis=0), sep='\n')
print('arr_mean_row: ', arr.mean(axis=1), sep='\n')