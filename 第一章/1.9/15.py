import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(0,1,0.02)
t1 = np.arange(-1,0,0.02)
g1 = 3 * t
g2 = 3 * (-t1)
plt.plot(t,g1,linestyle='-')
plt.plot(t1,g2,linestyle='-')
plt.hlines(0,-1,1)

plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
plt.title('信号的折叠')
plt.xlabel('t')
plt.ylabel('g(t)')
plt.show()