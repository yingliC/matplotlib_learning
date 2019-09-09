'''
八种内建默认颜色缩写：
    b: blue
    g: green
    r: red
    c: cyan
    m: magenta
    y: yellow
    k: black
    w: white
其他颜色表示方法
    灰色阴影
    html 十六进制
    RGB元祖
'''



'''
23种点形状。注意，不同点形状默认使用不同颜色
    "." : point        "v" : triangle_down
    "," : pixel        "^" : triangle_up
    "0" : circle       "<" : triangle_left
    "1" : tri_down     ">" : triangle_right
    "2" : tri_up       "s" : square
    "3" : tri_left     "p" : pentagon
    "4" : tri_right    "*" : star
    "8" : octagon      "h" : hexagon1
    "+" : plus         "H" : hexagon2
    "x" : x            "D" : diamond
    "d" : thin_diamond
'''



'''
四种线型
    -    实线
    --   虚线
    -.   点划线
    :    点线

'''



'''
样式字符串(可以将颜色、点型、线型写成一个字符串)，如：
    cx--
    mo:
    kp-

'''

'''
使用plt.style.use() 来美化坐标，参数‘ggplot’很好看
'''

import numpy as np
import matplotlib.pyplot as plt


y = np.arange(1,5)


# 颜色举例
# plt.plot(y,color='g') # 内置颜色

# plt.plot(y+1,color='0.5') #灰度

# plt.plot(y+2,color='#CDCDB4') # 十六进制

# plt.plot(y+3,color=(0.1,0.2,0.3)) # RGB元祖




# 点形状(写marker会将点连成线，不写则不连线)
# plt.plot(y,marker='o')

# plt.plot(y+1,marker='^')

# plt.plot(y+2,'D')

# plt.plot(y+3,'p')

# 线型
# plt.plot(y,'--')

# plt.plot(y+1,'-.')

# plt.plot(y+2,'-')

# plt.plot(y+3,':')

#样式字符串
plt.plot(y,'cx--')

plt.plot(y+1,'kp-.')

plt.plot(y+2,'mo-')

plt.plot(y+3,'y^:')


plt.show()
