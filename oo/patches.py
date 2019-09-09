'''
生成形状patches
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots()

xy1 = np.array([0.2,0.2])
xy2 = np.array([0.2,0.8])
xy3 = np.array([0.8,0.2])
xy4 = np.array([0.8,0.8])

circle = mpatches.Circle(xy1,0.05)
ax.add_patch(circle)

rect = mpatches.Rectangle(xy2,0.2,0.2, color='c')
ax.add_patch(rect)

polygon = mpatches.RegularPolygon(xy3,5,0.1, color='g')
ax.add_patch(polygon)

ellipse = mpatches.Ellipse(xy4,0.4,0.2,color='y')
ax.add_patch(ellipse)

plt.axis('equal')


plt.show()



