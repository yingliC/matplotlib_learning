'''
饼状图：
饼状图显示一个数据系列中各项的大小与各项总和的比例
饼状图中的数据点显示为整个饼状图的百分比
'''

import matplotlib.pyplot as plt


labels = 'A','B','C','D'
fracs = [15,30,45,10]

plt.axes(aspect=1) # 使x与y的比例为1：1

'''
x:饼状图的数据
labels：各个数据的标签
autopct：在饼状图上显示各个数据的多少
explode：突出显示某标签的数据
'''
explode = [0,0.05,0,0] # 每个标签数据块距离圆中心的位置
plt.pie(x=fracs,labels=labels,autopct='%.0f%%',explode=explode)


plt.show()

