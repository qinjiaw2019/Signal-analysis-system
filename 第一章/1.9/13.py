import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


t = np.arange(0,9,0.01)
y1 = 2 * np.exp(-0.5 * t)
plt.plot(t,y1,linestyle='-.')
y2 = y1 * np.sin(2 * np.pi * t)
plt.plot(t,y2)
y3 = -2 * np.exp(-0.5 * t)
plt.plot(t,y3,linestyle='-.')

plt.hlines(0,0,10)
plt.title('单边衰减指数信号')
plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.show()