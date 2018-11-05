import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

A = 2
a1 = -0.5
a2 = 0
a3 = 0.5

plt.ylim(-0.5,5)
plt.xlim(-3,3)

t = np.arange(-5,5,0.01)
y1 = A * np.exp(a1 * t)
plt.plot(t,y1)
y2 = 2 * np.exp(a2 * t)
plt.plot(t,y2)
y3 = 2 * np.exp(a3 * t)
plt.plot(t,y3)
plt.axvline(0,-5,5)
plt.axhline(0,-5,5)

plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.title('实指数信号,A=2,|a|=0.5')

plt.show()
