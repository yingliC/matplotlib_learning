'''
matplotlib对象简介
    FigureCanvas : 画布
    Figure       : 图
    Axes         : 在figure上生成的坐标轴，即实际画图的地方
'''



import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot()
t = ax.set_title("sin(x)")
plt.plot(x,y)

plt.show()

