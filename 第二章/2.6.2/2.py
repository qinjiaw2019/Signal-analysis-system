import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

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


T = 0.01
t1 = -2
t2 = 3
t3 = -1
t4 = 2

t5 = np.arange(t1,t2,T)
t6 = np.arange(t3,t4,T)

f1 = unit(t5+1)-unit(t5-2)

f2 = 3*(unit(t6)-unit(t6-2))

plt.subplot(311)
plt.plot(t5,f1)
plt.xlim(t1+t3,t2+t4)
plt.ylim(min(f1),max(f1)+0.5)
plt.ylabel('f1(t)')
plt.title('例2.6-2卷积')

plt.subplot(312)
plt.plot(t6,f2)
plt.xlim(t1+t3,t2+t4)
plt.ylim(min(f2),max(f2)+0.5)
plt.ylabel('f2(t)')

t1_ =np.linspace(-1.5,3,400)
t2_ = t1_

t,y = fconv(f1,f2,t1_,t2_)
plt.subplot(313)
plt.plot(t,y)
plt.ylabel('y(t)')


plt.show()


