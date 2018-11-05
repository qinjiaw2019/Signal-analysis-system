import numpy as np
from pylab import mpl
from scipy.signal import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


b = [1]
a = [1,3,2]
A,B,C,D = tf2ss(b,a)
sys = lti(A,B,C,D)
t = np.arange(0,10,0.01)
f = -2 * np.exp(-t)
zi = [0,0]
tout,y,x = lsim(sys,f,t,zi)
plt.plot(t,y)
plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
plt.xlabel('时间t')
plt.ylabel('y(t)')
plt.title('系统的零状态响应')

plt.show()