# -*- coding:utf8 -*-
# @TIME     :2019/5/30 14:30
# @Author   : 洪松
# @File     : 通用函数.py

import numpy as np
arr = np.arange(10)
print('arr: ', arr, sep='\n')

'''一元函数'''
print('arr_sqrt: ', np.sqrt(arr), sep='\n')
print('arr_exp: ', np.exp(arr), sep='\n')

'''二元函数'''
x = np.random.randn(8)
y = np.random.randn(8)
print('x: ', x, sep='\n')
print('y: ', y, sep='\n')
print('np.maximum(x, y): ', np.maximum(x, y), sep='\n') # 元素级最大值

arr_1 = np.random.randn(7)
print('np.modf(arr): ', np.modf(arr), sep='\n')

