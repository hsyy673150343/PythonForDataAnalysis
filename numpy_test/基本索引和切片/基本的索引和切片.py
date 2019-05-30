# -*- coding:utf8 -*-
# @TIME     :2019/5/29 20:38
# @Author   : 洪松
# @File     : 基本的索引和切片.py

import numpy as np

arr = np.arange(10)
print(arr)
print(arr[5])

print(arr[5:8])
# 当你将一个标量值赋值给一个切片时，该值会自动传播到整个选区
# 跟列表的重要区别在于，数组切片是原始数组的视图，这意味着数据不会被复制，视图上的任何修改都会直接反映到源数组上
# 如果想得到的是一份副本而非视图，就需要显式地进行复制操作，例如arr[5:8].copy()
arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
arr_slice[1] = 12345
print(arr)

arr_slice[:] = 64
print(arr)

# x = arr[5:8].copy()
# print(x)


arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[2])
print(arr_2d[0][2])
print(arr_2d[0, 2])



arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d)
print(arr_3d.ndim)
print(arr_3d[0])

old_values = arr_3d[0].copy()
arr_3d[0] = 42
print(arr_3d)

arr_3d[0] = old_values
print(arr_3d)

print('arr_2d:\n ', arr_2d)
print(arr_2d[:2])

# 0,1行的第一列之后的所有元素
print(arr_2d[:2, 1:])
# 第一行的前两个元素
print(arr_2d[1, :2])
# 第二行的第一个元素
print(arr_2d[2, :1])
# 只有冒号表示选取整个轴,即0，1，2行的第一个元素
print(arr_2d[:,: 1])

arr_2d[:, :1] = 0
print(arr_2d)