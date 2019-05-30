# -*- coding:utf8 -*-
# @TIME     :2019/5/30 15:27
# @Author   : 洪松
# @File     : test2.py
import numpy as np
'''将条件逻辑表述为数组运算'''

x_arr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y_arr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
# 当cond中的值为True时, 选取x_arr的值，否则从y_arr中选取
'''
列表推导式的写法：
对大数组的处理速度不是很快
无法用于多维数组
'''
result1 = [(x if c else y) for x, y, c in zip(x_arr, y_arr, cond)]
print('result1: ', result1)
'''
numpy.where() 有两种用法：

1.np.where(condition, x, y)
满足条件(condition)，输出x，不满足输出y。

2. np.where(condition)
只有条件 (condition)，没有x和y，则输出满足条件 (即非0) 元素的坐标 (等价于numpy.nonzero)。
这里的坐标以tuple的形式给出，通常原数组有多少维，输出的tuple中就包含几个数组，分别对应符合条件元素的各维坐标。

'''
'''np.where的写法'''
result2 = np.where(cond, x_arr, y_arr)
print('result2: ', result2)

result3 = np.where(cond)
print('result3: ', result3)


arr = np.random.randn(4, 4)
print('arr: ', arr, sep='\n')

arr_1 = np.where(arr > 0, 2, -2)
print('arr_1: ', arr_1, sep='\n')