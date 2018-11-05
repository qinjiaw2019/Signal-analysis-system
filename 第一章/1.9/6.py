import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(-2 * np.pi,2 * np.pi,0.001)
y = np.sin(2 * np.pi * t)/(2 * np.pi * t)
y =  y +(y==0) * np.spacing(y)
plt.plot(t,y)

plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.title('抽样信号Sa(at),a=2π')
plt.grid(color='black' , linewidth='0.5' ,linestyle='--')

plt.show()