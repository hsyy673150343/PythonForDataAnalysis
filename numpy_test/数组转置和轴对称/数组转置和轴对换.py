# -*- coding:utf8 -*-
# @TIME     :2019/5/29 21:48
# @Author   : 洪松
# @File     : 数组转置和轴对换.py

import numpy as np


'''transpose()'''
'''
二维
'''
arr_1 = np.arange(4).reshape((2,2))
print('arr_1: ', arr_1, sep='\n')
# 对于二维 ndarray，transpose在不指定参数时默认是矩阵转置。
print('arr_1.transpose(): ', arr_1.transpose())

print('arr_1.transpose(0, 1):',arr_1.transpose(0, 1), sep='\n')
# 相当于转置
'''
arr_1[0][0] == 0
arr_1[0][1] == 1
arr_1[1][0] == 2
arr_1[1][1] == 3
我们不妨设第一个方括号"[]"为 0轴 ，第二个"[]"为 1轴 ，则arr_1可在 0-1坐标系 下表示如下： 见图片1
因为 arr_1.transpose((0,1)) 表示按照原坐标轴改变序列，也就是保持不变
而 arr_1.transpose((1,0)) 表示交换 ‘0轴’ 和 ‘1轴’，所以就得到如下图所示结果：见图片2
注意，任何时候你都要保持清醒，告诉自己第一个方括号"[]"为 0轴 ，第二个"[]"为 1轴 
此时，transpose转换关系就清晰了。
'''
print('arr_1.transpose(1, 0):',arr_1.transpose(1, 0), sep='\n')

'''
三维
'''
arr_2 = np.arange(16).reshape(2, 2, 4)
print('arr_2: ', arr_2, sep='\n')
'''
对上述的arr_2表示成如下三维坐标的形式：见图片3
所以对于如下的变换都很好理解啦： 
'''
print('arr_2.transpose(0, 1, 2): ', arr_2.transpose(0, 1, 2), sep='\n') # 保持arr_2不变
print('arr_2.transpose(1, 0, 2): ', arr_2.transpose(1, 0, 2), sep='\n') # 0轴和1轴交换
'''
见图片4, 根据图4 arr_2.transpose(1, 0, 2)[0][1][2]的值为10
'''
print('arr_2.transpose(1, 0, 2)[0][1][2]: ', arr_2.transpose(1, 0, 2)[0][1][2], sep='\n')

'''swapaxes()---轴对称'''
print('arr_2.swapaxes(1, 2): ', arr_2.swapaxes(1, 2), sep='\n')

