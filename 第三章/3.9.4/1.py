import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(0,1,0.0005)
f = 8
xa = np.cos(2*np.pi*f*t)
plt.subplot(211)
plt.plot(t,xa)
plt.grid(color='black' , linewidth='0.5' ,linestyle='--')
plt.xlabel('t/sec')
plt.ylabel('幅值')
plt.title('连续信号x(t)')
plt.xlim(0,1)
plt.ylim(-1.2,1.2)

plt.subplot(212)
T=0.0625
n=np.arange(0,1,T)
xs = np.cos(2*np.pi*f*n)
k = np.arange(0,len(n))
print(k.shape,xs.shape)
plt.stem(k,xs)
plt.grid(color='black' , linewidth='0.5' ,linestyle='--')
plt.xlabel('n/sec')
plt.ylabel('幅值')
plt.title('离散信号x(n)')
plt.xlim(0,16)
plt.ylim(-1.2,1.2)

plt.show()