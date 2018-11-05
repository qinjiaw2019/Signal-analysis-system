import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

N=5000
T=0.1
n=np.arange(1,N)
D = 2 *np.pi/(N*T)
f = np.sin(5*n*T)
F = T*np.fft.fftshift(np.fft.fft(f))
k = []
for i in np.arange(-(N-1)/2,N/2-1):
    k.append(np.floor(i))
k = np.array(k)

plt.subplot(311)
plt.plot(n*T,f)
plt.xlim(-1,50)
plt.ylim(-1.1,1.1)
plt.axhline(0,-1,50)
plt.ylabel('f(t)')

plt.subplot(312)
plt.plot(k*D,np.abs(F))
plt.ylabel('振幅')
plt.xlim(-8,8)
plt.ylim(-0.1,300)

plt.subplot(313)
plt.plot(k*D,np.angle(F))
plt.ylabel('相位')
plt.xlim(-8,8)
plt.ylim(-2,2)

plt.show()