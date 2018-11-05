import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(-5,5,0.001)
y =  np.sign(t)
plt.plot(t,y)
plt.vlines(0,-1.5,1.5)
plt.hlines(0,-5,5)

plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.title('符号信号')

plt.show()