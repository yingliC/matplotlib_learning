import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,11,1)

y = x*x

plt.plot(x,y)

# xy: 表示注释的起始点,xytext:表示注释文字的起始坐标, arrowprops: 表示注释图形的样式
plt.annotate('this is the bottom',xy=(0,1),xytext=(0,20),arrowprops=dict(facecolor='r',headlength=30,headwidth=30))

plt.show()

