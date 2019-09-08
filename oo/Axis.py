import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
import datetime


'''
坐标轴范围调整
'''
# x = np.arange(-10,11,1)
# plt.plot(x,x*x)

# plt.axis() 里面有4个数，从左到右分别为x的最小坐标，x的最大坐标，y的最小坐标，y的最大坐标
# 直接传数组就改变了坐标轴的取值范围
# plt.axis([-5,5,20,60])

# plt.xlim([-5,5]) # 仅调整x轴的坐标范围，同理ylim为仅调整y轴的坐标范围

# plt.xlim(xmin=-5) # 若仅想调整一边，则只写想调整的参数即可，如这里只想调整x轴的最小范围，而不调整最大范围


'''
坐标轴的刻度调整

'''
# x = np.arange(1,11,1)
# plt.plot(x,x)

# ax = plt.gca() # 获取当前图形的坐标轴

# # nbins：（重要参数）坐标轴总共有多少格
# # ax.locator_params(nbins=5)

# ax.locator_params('y',nbins=10) # 可指定要调整的坐标轴

# # 时间坐标轴
# fig = plt.figure()
# start = datetime.datetime(2019,1,1)
# stop = datetime.datetime(2020,1,1)
# delta = datetime.timedelta(days=1) # 1天为时间间隔

# dates = mlp.dates.drange(start,stop,delta) # 将日期转换成matplotlib认得的dates序列

# y = np.random.rand(len(dates))
# ax = plt.gca()

# ax.plot_date(dates,y,linestyle='-',marker='')

# date_format = mlp.dates.DateFormatter('%Y-%m') # 修改日期的格式
# ax.xaxis.set_major_formatter(date_format)

# fig.autofmt_xdate() # 将日期的排列根据图形的大小自适应





'''
双坐标轴
'''
x = np.arange(2,20,1)
y1 = x*x
y2 = np.log(x)

# plt.plot(x,y1)

# plt.twinx() # 在一个图形上添加里一个坐标轴

# plt.plot(x,y2,'r')


# 面向对象的方式
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.plot(x,y1)
ax1.set_ylabel('Y1')

ax2 = ax1.twinx()

ax2.plot(x,y2,'r')
ax2.set_ylabel('Y2')

ax1.set_xlabel('Compare Y1 and Y2')



plt.show()