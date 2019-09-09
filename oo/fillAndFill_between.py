'''
对曲线下面或者曲线之间的区域进行填充
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5*np.pi,100)

y1 = np.sin(x)
y2 = np.sin(2*x)

# plt.plot(x,y1)
# plt.plot(x,y2)


# plt.fill(x,y1,'b',alpha=0.3)

# plt.fill(x,y2,'r',alpha=0.3)

fig = plt.figure()

ax = plt.gca()

ax.plot(x,y1,color='r')
ax.plot(x,y2,color='g')

# interpolate : 当x值较稀疏处于离散时，该参数设为True，会将空白的地方也填充
# 原理：自动计算两条线交点的位置予以填充
ax.fill_between(x,y1,y2,where=y1>y2,facecolor='y',interpolate=True)
ax.fill_between(x,y1,y2,where=y1<y2,facecolor='m')


plt.show()


