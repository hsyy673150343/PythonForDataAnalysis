# -*- coding:utf8 -*-
# @TIME     :2019/5/30 21:58
# @Author   : 洪松
# @File     : test2.py

import matplotlib.pyplot as plt
'''plt.subplots可以创建一个新的Figure,并返回一个含有已创建的subplot对象的numpy数组'''
'''
subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True,
             subplot_kw=None, gridspec_kw=None, **fig_kw)
参数的含义见图1
'''
fig, axes = plt.subplots(2, 3)
print(axes)