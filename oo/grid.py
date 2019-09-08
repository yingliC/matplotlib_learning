'''

'''

import numpy as np
import matplotlib.pyplot as plt

# y = np.arange(1,5)
# plt.plot(y,y*2)

# # plt.grid(True)
# plt.grid(color='r',linewidth='2',linestyle=':')


x = np.arange(0,10,1)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,x*2)
ax.grid(color='g',linestyle=':')

plt.show()

