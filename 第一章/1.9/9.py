import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(0,5,0.01)
a1 = 1 #斜率
y = a1 * t
plt.plot(t,y)
plt.hlines(0,0,5,color='gray',linewidth=0.5)
plt.vlines(0,0,5,color='gray',linewidth=0.5)

plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.title('斜坡信号')

plt.show()