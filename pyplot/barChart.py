'''
条形图：
以长方形的长度为变量的统计图表
用来比较多个项目分类的数据大小
通常利用与较小的数据集分析
'''

import numpy as np
import matplotlib.pyplot as plt

# N = 5
# y = [20,10,30,25,15]
# index = np.arange(N)

# p1 = plt.bar(index, y) # index：条形图的横坐标，y：条形图的高度
# plt.bar(index, y, color='y', width=0.4)

# plt.bar(0,bottom=index,height=0.5,width=y,orientation='horizontal') # 水平图方法一，手动设置
# plt.barh(index,width=y,height=0.5,left=0) # 水平图方法二，直接用水平图函数



index = np.arange(4)
scales_BJ = [52,55,63,53]
scales_SH = [44,66,55,41]

bar_width = 0.3

# 并列的条形图
# plt.bar(index,scales_BJ,bar_width,color='b')
# plt.bar(index+bar_width,scales_SH,bar_width,color='r')

# 层叠的条形图
plt.bar(index,scales_BJ,bar_width,color='b')
plt.bar(index,scales_SH,bar_width,color='r',bottom=scales_BJ) # 底部不从0开始而是从上一个直方图开始接着画


plt.show()

