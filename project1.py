'''
三种方式：
pyplot:经典高层封装，到目前为止
pylab： 将matplotlib 和 numpy 合并的模块，模拟matlab的编程环境
面向对象的方式：matplotlib的精髓，更基础和底层的方式


三种方式的优劣：
pyplot：简单易用。交互使用方便，可以根据命令实时作图，但底层能力不足。
pylab： 完全封装，环境最接近matlab。不推荐使用
面向对象（Object—Oriented）的方式：接近Matplotlib基础和底层的方式，难度稍大。但定制能力强。而且是Matplotlib的精髓。

总结：实战中推荐，根据需求，综合使用pyplot和OO的方式，显示导入numpy
'''


'''
pyplot 形式
'''
# import matplotlib.pyplot as plt
# import numpy as np
# # plt.plot([1,2,3,4],[-4,-3,-2,-1]) # 第一 个[]为x轴，第二个[]为y轴
# # plt.plot([1,2,3,4],[-1,-2,-3,-4])

# x = np.arange(0,10,1)
# y = np.random.randn(len(x))
# plt.plot(x,y)
# plt.title('pyplot')

# plt.show()



''' 
pylab 形式
'''
# from pylab import *

# x = arange(0,10,1)
# y = randn(len(x))

# plot(x,y)
# title('pylab')
# show()

'''
面向对象的方式
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10,1)
y = np.random.randn(len(x))

fig = plt.figure()
ax = fig.add_subplot()
l,=plt.plot(x,y)
t = ax.set_title('object oriented')

plt.show()




