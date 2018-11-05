import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from sympy import *
from sympy.abc import x,y

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def unit(t):
    r = np.where(t>0.0,1.0,0.0)
    return r
def fconv(f1,f2,t1,t2):
    d = 0.01
    f = np.convolve(f1,f2)
    f = f*d
    ts = t1[0]+t2[0]
    l = np.size(f1)+np.size(f2)-1
    t = np.linspace(ts,ts+l*d,l)
    return t,f

def stepfun(t,t0):
    y = []
    for i in t:
        if i>=t0:
            y.append(1)
        else:
            y.append(0)
    return np.array(y)

T = 0.02
# t = np.arange(-10,10,T)

N = 200
t = np.linspace(-10,10,2*N)
W = 4*np.pi
k=np.arange(-N,N)
w = k * W/N
f1 = stepfun(t,-1)-stepfun(t,1)

plt.subplot(311)
plt.plot(t,f1)
plt.xlim(-3,3)
plt.ylim(-0.1,1.2)
plt.title('f(t)')
plt.grid()

t.shape = t.shape[0],1
w.shape = 1,w.shape[0]
print(t)
F = T * f1 * np.exp(-1j*t.T * w) #f(t)的傅里叶变换
F1 = abs(F)

P1 = np.angle(F)
plt.subplot(312)
plt.plot(w.T,F1.T)
plt.xlim(-3*np.pi,3*np.pi)
# plt.ylim(-0.01,2.1)
plt.xlabel('w')
plt.ylabel('振幅')

plt.subplot(313)
plt.plot(w,P1*180/np.pi)
# plt.xlim(-3*np.pi,3*np.pi)
# plt.ylim(-180,180)
plt.xlabel('w')
plt.ylabel('相位(度)')

plt.show()
