# -*- coding:utf8 -*-
# @TIME     :2019/5/29 19:55
# @Author   : 洪松
# @File     : 创建ndarray.py

import numpy as np

data_1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data_1)
print('arr1: ', arr1)

data_2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data_2)
print('arr2: ',arr2)
print('arr2.ndim: ', arr2.ndim)
print('arr2.shape: ', arr2.shape)
print('arr2.dtype:', arr2.dtype)
print('arr1.dtype: ', arr1.dtype)

arr3 = np.zeros(10)
print('arr3: ', arr3)

arr4 = np.zeros((3, 6))
print('arr4: ', arr4)

arr5 = np.empty((2, 3, 2))
print('arr5: ', arr5)


arr6 = np.arange(15)
print('arr6: ', arr6)

# 可以通过ndarray的astype方法显式地转换其dtype
# 调用astype无论如何都会创建一个新的数组(原始数据的一份拷贝),即使新的dtype跟老的dtype相同也是如此
print('arr6.dtype: ', arr6.dtype)
float_type = arr6.astype(np.float64)
print('更改后的arr6.dtype: ', float_type.dtype)


