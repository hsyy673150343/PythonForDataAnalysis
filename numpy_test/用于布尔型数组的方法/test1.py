# -*- coding:utf8 -*-
# @TIME     :2019/5/30 16:07
# @Author   : 洪松
# @File     : test1.py

import numpy as np

arr = np.random.randn(100)
print('arr: ', arr, sep='\n')

print('正值的数量：', (arr > 0).sum())

bool = np.array([False, False, True, False])
print('数组中是否存在一个或多个True: ', bool.any())
print('数组中所有值是否都是True: ', bool.all())