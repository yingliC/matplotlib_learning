'''
箱型图：
箱型图又称为盒须图、盒式图或箱线图
是一种用作显示一组数据分散情况资料的统计图
上边缘，上四分位数，中位数，下四分位数，下边缘，异常值
'''

# 箱型图可以同时画几组数据

import numpy as np
import matplotlib.pyplot as plt

# data = np.random.normal(size=1000,loc=0,scale=1)

# # sym：调整异常值的点的形状, whis:调整上边缘与上四分位数之间的线的长度
# plt.boxplot(data,sym='o',whis=0.3)




data = np.random.normal(size=(1000,4),loc=0,scale=1)

labels = ['A','B','C','D']



plt.boxplot(data,sym='o',labels=labels)





plt.show()


