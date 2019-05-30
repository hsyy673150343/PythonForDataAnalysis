# -*- coding:utf8 -*-
# @TIME     :2019/5/29 20:34
# @Author   : 洪松
# @File     : 数组和标量之间的运算.py

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr * arr)
print(arr - arr)
# 不同大小的数组之间的运算叫做广播
print(1/arr)
print(arr ** 0.5)


