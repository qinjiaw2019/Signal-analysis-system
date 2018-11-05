import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(0,2,0.0001)
f = np.sin(2 * np.pi * t)
f1 = np.sin(2 * np.pi * (t-0.2))
plt.plot(t,f,linestyle='-')
plt.plot(t,f1,linestyle='-')

plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
plt.title('信号的位移')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.show()