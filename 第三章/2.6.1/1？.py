import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题



N = 5000
T = 0.01
n = np.arange(1,8*N+1)
D = 2*np.pi/(N*T)
f = np.square(2 * np.pi * n * T)


#产生方波
F = T * np.fft.fftshift(np.fft.fft(f))
k = []
for i in np.arange(-(8*N-1)/2,8*N/2):
    # if np.sin(i)>0:
    #     k.append(-1)
    # else:
    #     k.append(1)
    k.append(np.floor(i))

k = np.array(k)
print(k)

plt.subplot(211)
plt.plot(n*T,f)
plt.xlim(0,10)
plt.ylim(-1.5,1.5)
plt.ylabel('f(t)')
plt.axhline(0,-1,10)

# print(k*D)
# print(abs(F))

plt.subplot(212)
plt.plot(k*D,abs(F))
#
# plt.ylabel('幅频')
# plt.xlim(-1000,1000)
# plt.ylim(-10,300)


plt.show()
