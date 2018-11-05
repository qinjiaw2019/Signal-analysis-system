import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def stepfun(t,t0):
    y = []
    for i in t:
        if i>=t0:
            y.append(1)
        else:
            y.append(0)
    return np.array(y)

T=0.02

N = 200
t = np.linspace(-10,10,2*N)
W = 4*np.pi
k = np.arange(-N,N)
w = k*W/N


f1 = stepfun(t,0)-stepfun(t,2) #f(t)


plt.subplot(311)
plt.plot(t,f1)
plt.xlim(-2,2)
plt.ylim(-0.1,1.2)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('f(t)')
plt.grid()

F = T * f1 * np.exp(-1j * t.T*w)
F1 = np.abs(F)
P1 = np.angle(F)

plt.subplot(312)
plt.plot(w,F1)
plt.ylabel('振幅')
plt.grid()

plt.subplot(313)
plt.plot(w,P1*180/np.pi)
plt.xlim(-3*np.pi,3*np.pi)
plt.ylim(-180,180)
plt.show()