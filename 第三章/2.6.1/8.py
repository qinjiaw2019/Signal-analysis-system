import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from sympy import *

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

N = 5000
T = 0.1
n = np.arange(1,N)
D = 2*np.pi/(N*T)
f=-1+2*np.sin(0.2*np.pi*n*T)-3*np.cos(np.pi*n*T)
F = np.fft.fftshift(np.fft.fft(f))

k = []
for i in np.arange(-(N-1)/2,N/2-1):
    k.append(np.floor(i))
k = np.array(k)

plt.subplot(211)
plt.plot(n*T,f)
plt.xlim(-1,50)
plt.ylim(-6.1,4.1)
plt.axhline(0,0,50)
plt.axvline(0,-6.1,4.1)
plt.ylabel('f(t)')

plt.subplot(212)
plt.plot(k*D,np.abs(F))
plt.ylabel('幅频')
plt.xlim(-6,6)
plt.ylim(-0.1,800)

plt.show()