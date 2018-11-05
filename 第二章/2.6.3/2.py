from scipy.signal import *
import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

b = [1]
a = [1,0,1]
A,B,C,D = tf2ss(b,a)

sys = ss2tf(A,B,C,D)
t=np.arange(0,30,0.1)
f = np.cos(t)
a,y,x = lsim2(sys,f,t)

plt.plot(t,y)
plt.axhline(0,0,30)
plt.xlabel('时间(t)')
plt.ylabel('y(t)')
plt.title('系统的全响应')

plt.show()