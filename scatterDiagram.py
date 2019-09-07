'''
* 散点图显示两组数据的值，每个点的坐标位置由变量的值决定
* 由一组不连接的点完成，用于观察两种变量的相关性
* 例如身高-体重、温度-维度 等
'''
import numpy as np
import matplotlib.pyplot as plt

'''
散点图的外观调整常用的四个参数
* 颜色：c（默认‘b’，蓝色）
* 点的大小：s(代表面积)
* 透明度：alpha
* 点的形状：marker（默认‘o’，圆形）
'''

height = [161,170,182,175,173,165]
weight = [50,58,80,70,69,55]

# plt.scatter(height,weight)
# plt.scatter(height,weight,c='r')
# plt.scatter(height,weight,c='r',s=10)
plt.scatter(height,weight,c='r',s=10,marker='<')
plt.ylabel
plt.show()