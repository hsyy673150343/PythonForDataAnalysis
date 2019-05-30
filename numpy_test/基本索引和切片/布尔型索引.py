# -*- coding:utf8 -*-
# @TIME     :2019/5/29 21:11
# @Author   : 洪松
# @File     : 布尔型索引.py
import numpy as np


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Ioe', 'Joe'])
data = np.random.randn(7, 4)
print(names)
print(data)


print(names == 'Bob') # [ True False False  True False False False] 布尔型数组

# 布尔型数组的长度必须跟被索引的轴的长度一致，这里布尔型数组长度为7，被索引的data有7行数据，即轴为7
# 通过布尔型索引选取数组中的数据,将总是创建数据的副本，即使返回一模一样的数组也是如此
print(data[names == 'Bob'])

print(data[names == 'Bob', 2:])
print(data[names == 'Bob', 3])


print(names != 'Bob')# [False  True  True False  True  True  True]

# &(和) |(或)
# python关键字and和or在布尔型数组中无效
mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(data[mask])
# 将data中的所有负值都设置为0
data[data < 0] = 0
print(data)

data[names != 'Joe'] = 7
print(data)