# -*- coding:utf8 -*-
# @TIME     :2019/5/30 16:23
# @Author   : 洪松
# @File     : test1.py

import numpy as np

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print('找出数组中的唯一值并返回已排序的结果： ', np.unique(ints))

values = np.array([6, 0, 0, 3, 2, 5, 6])
print('测试一个数组中的值在另一个数组中的成员资格,返回一个布尔型数组：', np.in1d(values, [2, 3, 6]))