'''
matplotlib自带mathtext引擎，不需要安装TeX系统
$ 作为开始和结束符， 如“ $ y=x+z $ ”

'''

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)

ax.set_xlim([1,7])
ax.set_ylim([1,5])

# 在字符串前面写r ，代表字符串不转义
ax.text(2,4,r"$ \alpha_i \beta_j \pi \lambda \omega $",size=20)

ax.text(4,4,r"$ \sin(0)=\cos(\frac{\pi} {2}) $",size=20)

ax.text(2,2,r"$ \lim_{x \rightarrow y} \frac{1} {x^3} $",size=20)

ax.text(4,2,r"$ \sqrt[4]{x}=\sqrt{y} $",size=20)


plt.show()



