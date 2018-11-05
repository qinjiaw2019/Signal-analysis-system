import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

fs = 10000
t = np.arange(0,0.1,1/fs)
f0 = 50
sum = 0
plt.subplot(211)
for n in np.arange(1,9,2):
    plt.plot(t,4/np.pi*1/n*np.sin(2*np.pi*n*f0*t))
plt.title('信号叠加前')
plt.subplot(212)
for n in np.arange(1,9,2):
    sum = sum+4/np.pi*1/n*np.sin(2*np.pi*n*f0*t)
    plt.plot(t,sum)
plt.title('信号叠加后')
plt.show()