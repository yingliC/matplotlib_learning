'''
直方图:
由一系列高度不等的纵向条形组成，表示数分布的情况
例如某年级同学的身高分布情况
注意和条形图的区别：
    直方图通常用来显示连续性的数值型数据，分组是用连续的方式分组，并且是可以自定义的
    条形图通常用来展示不同类别的数据，类别通常是不能自定义的，而且是不连续的
'''

import numpy as np
import matplotlib.pyplot as plt


# mu = 100    # mean of distribution
# sigma = 20  # standard deviation of distribution
# x = mu + sigma * np.random.randn(20000)

# # plt.hist(x, bins=10,color='r',density=True) # bins:直方图中有几个直方, density:是否要对数据进行标准化

# plt.hist(x, bins=100,color='g',density=False)


# 双变量的直方图
x = np.random.randn(1000)+2
y = np.random.randn(1000)+3

plt.hist2d(x,y,bins=40)





plt.show()

