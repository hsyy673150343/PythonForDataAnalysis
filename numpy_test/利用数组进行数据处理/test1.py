# -*- coding:utf8 -*-
# @TIME     :2019/5/30 14:55
# @Author   : 洪松
# @File     : test1.py

import numpy as np

'''

使用meshgrid方法，你只需要构造一个表示x轴上的坐标的向量和一个表示y轴上的坐标的向量;然后作为参数给到meshgrid(),
该函数就会返回相应维度的两个矩阵;

'''
points = np.arange(-5, 5, 0.01) # 1000个间隔相等的点
print('points: ', points, sep='\n')
xs, ys = np.meshgrid(points, points)

print('xs :', xs, sep='\n')
print('ys :', ys, sep='\n')

# grid_cor = np.meshgrid(points, points)
# print(grid_cor)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
