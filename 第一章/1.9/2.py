import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

A = 2
a = -0.5
t = np.arange(0,10,0.01)
y = A * np.exp(a * t)
plt.plot(t,y)
plt.axvline(0,0,2,linestyle='--',color='gray')

plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.title('单边指数')
plt.show()
