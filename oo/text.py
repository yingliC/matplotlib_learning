import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10,11,1)

y = x * x

plt.plot(x, y)


# 画文字
# family: 字体 ，size: 字体大小 ， style: 字体倾斜度 ， weight: 字体粗细 , bbox: 给文字加框
plt.text(-2,40,'function: y=x^2',family='serif',size=20,style='oblique',weight='black') 
plt.text(-2,20,'function: y=x^2',family='fantasy',size=20,color='c',bbox=dict(facecolor='r',alpha=0.2))

plt.show()



