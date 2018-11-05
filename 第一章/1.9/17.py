import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(-0.9,0.9,0.02)
y1 = 3 * (t ** 2)
y2 = -3 * (t ** 2)
plt.plot(t,y1,linestyle='-')
plt.plot(t,y2,linestyle='--')
plt.axhline(0,-1,1)

plt.title('倒相')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()