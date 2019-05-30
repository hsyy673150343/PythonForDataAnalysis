# -*- coding:utf8 -*-
# @TIME     :2019/5/29 21:29
# @Author   : 洪松
# @File     : 花式索引.py
import numpy as np

arr = np.empty((8, 4))
print(arr)

for i in range(8):
    arr[i] = i

print(arr)

print(arr[[4, 3, 0, 1]])
# 使用负数索引将会从末尾开始选取行
print(arr[[-3, -5, -7]])


arr1 = np.arange(32).reshape((8, 4))
print(arr1)
# 有问题
# 一次传入多个索引数组会有一点特别，他返回的是一个一位数组，其中的元素对应各个索引元组
# print(arr[[1, 5, 7, 2]],[[0, 3, 1, 2]])
#
# print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])