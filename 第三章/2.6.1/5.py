import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from sympy import *
from sympy.abc import t,x

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

N = -500
T = 0.1
n = np.arange(-1,N,-1)
D = 2 * np.pi/(N*T)
f = np.exp(0.1*n*T)


plt.subplot(311)
plt.plot(n*T,f)
plt.ylabel('f(t)')
plt.axhline(0,-50,0)
plt.axvline(0,0,1)
plt.xlim(-50,1)
plt.ylim(-0.1,1.2)
plt.ylabel('f(t)')


F =  T * np.fft.fftshift(np.fft.fft((f)))
# F =  fourier_transform(exp(0.1*x),t,x)
# plot(abs(F_))
k = []
for i in np.arange(-(-N-1)/2,-N/2-1):
    k.append(np.floor(i))
plt.subplot(312)
k = np.array(k)

plt.plot(k*D,abs(F))
plt.ylabel('幅频')
plt.xlim(-2,2)
plt.ylim(-0.1,10)

plt.subplot(313)
plt.plot(k*D,np.angle(F))
plt.ylabel('相频')
plt.xlim(-2,2)
plt.ylim(-2,2)
#
#
plt.show()