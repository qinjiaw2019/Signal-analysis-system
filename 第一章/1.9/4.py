import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(0,9,0.01)
A = 2
a = -0.5
y = np.cos(2 * np.pi * t)
y1 = A * np.exp(a * t)
plt.plot(t,y1,linestyle='-.',linewidth=1,color='gray')
y2 = y1 * y
plt.plot(t,y2)
plt.axhline(0,0,10)
y3 = -2 * np.exp(-0.5 * t)
plt.plot(t,y3,linestyle='-.',linewidth=1,color='gray')


plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.title('单边衰减指数信号')

plt.show()