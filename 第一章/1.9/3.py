import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(-1,2,0.001)
y = np.sin(2 * np.pi * t + np.pi/3)
plt.plot(t,y)

plt.axvline(0,-1.5,1.5,color='gray',linewidth=0.5)
plt.axhline(0,-1,2,color='gray',linewidth=0.5)

plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.title('正弦信号')

plt.show()