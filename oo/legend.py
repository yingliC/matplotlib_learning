import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,11,1)


# plt.plot(x,x*2,label='Normal')
# plt.plot(x,x*3,label='Fast')
# plt.plot(x,x*4,label='Faster')
# # loc : 位置， ncol : 几列
# plt.legend(loc=0,ncol=2)



# # 直接将label以数组的形式写在legend里面
# plt.plot(x,x*2)
# plt.plot(x,x*3)
# plt.plot(x,x*4)

# plt.legend(['Normal','Fast','Faster'])


# 面向对象的方式：
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,x)

ax.legend(['ax legend'])




plt.show()

