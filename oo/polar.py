'''
极坐标
'''
import numpy as np
import matplotlib.pyplot as plt

r = np.arange(1,6,1)
theta = [0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]

# 画极坐标时添加参数projection（投影），polar(极坐标)，将坐标系投影为极坐标
ax = plt.subplot(111,projection='polar')

ax.plot(theta,r,color='r',linewidth=3)

ax.grid(True)

plt.show()


