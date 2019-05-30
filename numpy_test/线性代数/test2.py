# -*- coding:utf8 -*-
# @TIME     :2019/5/30 16:40
# @Author   : 洪松
# @File     : test2.py

from numpy.linalg import  inv, qr
import numpy as np

X = np.random.randn(5, 5)
'''求矩阵X的内积'''
mat = X.T.dot(X)
print('X的内积：', mat, sep='\n')
print('mat的逆：', inv(mat), sep='\n')
print('单位化矩阵mat: ', mat.dot(inv(mat)), sep='\n')
q, r = qr(mat)
print('QR分解： ', q, r, sep='\n')