# -*- coding:utf8 -*-
# @TIME     :2019/5/30 21:40
# @Author   : 洪松
# @File     : test1.py

import matplotlib.pyplot as plt
import numpy as np
''' matplotlib的图像都位于Figure对象中。'''
fig = plt.figure()
'''不能通过空Figure绘图，必须用add_subplot创建一个或多个subplot才行'''
# 图像是2x2的,且当前选中的是4个subplot中的第一个(编号从1开始)...以此类推
ax1 = fig.add_subplot(2, 2, 1)
print(ax1)

ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
# k--是一个线型选项,用于告诉matplotlib绘制黑色虚线图
plt.plot(np.random.randn(50).cumsum(), 'k--')
'''
fig.add_subplot所返回的对象是AxesSubplot,直接调用它们的实例方法就可以
在其它空着的格子里画图了
'''
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.show()