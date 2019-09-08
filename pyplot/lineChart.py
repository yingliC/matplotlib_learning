'''
折线图是用直线段将各数据连接起来组成的图形
常用来观察数据随某一变量变化的趋势
'''
import numpy as np
import matplotlib.pyplot as plt
'''
主要的三个参数：
线性：linestyle
颜色：color
点形状：marker
'''

# x = np.linspace(-10,10,100) # 生成一组等区间的数值，从-10开始到10，平均分成100份
x = np.linspace(-10,10,5)
y1 = x**2
y2 = 2*x

x1 = np.arange(0,10,0.1)
y3 = np.sin(x1)

# plt.plot(x,y1,linestyle='--',color='r',marker='<')
# plt.plot(x,y2,linestyle='-',color='y',marker='o')
# plt.plot_date(date,y,linestyle='-') # 专门绘制有一个坐标轴是时间的图，默认是散点图，可以加上‘-’使其变成折线图
plt.plot(x1,y3,color='g')

plt.show()

