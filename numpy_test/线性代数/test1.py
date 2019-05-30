# -*- coding:utf8 -*-
# @TIME     :2019/5/30 16:33
# @Author   : 洪松
# @File     : test1.py

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 23], [-1, 7], [8, 9]])
print('x: ', x, sep='\n')
print('y：', y, sep='\n')
print('x*y: ', np.dot(x, y), sep='\n')
print('x*y: ', x.dot(y), sep='\n')
print('one_dimension: ', np.dot(x, np.ones(3)), sep='\n')

