import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def deriv(f):
	dx=0.00000001
	return lambda x: (f(x+dx)-f(x))/dx

t0 = 0
t1 = -1
t2 = 3
dt = 0.001
t = np.arange(t1,t2,dt)
n = len(t)
k1 = np.floor((t0-t1)/dt)
y = np.zeros(n)
y = diff(k1)

# plt.plot(t,y)
plt.xlabel('时间t')
plt.ylabel('幅值y')
plt.title('实指数信号,A=2,|a|=0.5')

plt.show()