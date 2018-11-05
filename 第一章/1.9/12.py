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

T = 0.01
t = np.arange(0,10,T)
t1 = np.arange(0,10,0.01)
f1 = stepfun(t,0)-stepfun(t,4)
f2 = np.cos(2 * np.pi * t1)
y = f1 + f2
plt.subplot(311)
plt.plot(t,f1)
plt.title('信号相加')
plt.ylabel('f1')

plt.subplot(312)
plt.plot(t,f2)
plt.ylabel('f2')

plt.subplot(313)
plt.plot(t,y)
plt.ylabel('y')
plt.xlabel('时间t')
plt.axhline(0,0,10)

plt.show()