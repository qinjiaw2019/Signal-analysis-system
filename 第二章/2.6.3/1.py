from scipy.signal import lti,impulse2,lsim2
import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import mpl


b = [1]
a = [1,0,1]

sys = lti(b,a)
t=np.arange(0,10,0.1)
f = np.cos(2 * math.pi * t)
a,y,x = lsim2(sys,f,t)

plt.plot(t,y)

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.xlabel('时间(t)')
plt.ylabel('y(t)')
plt.title('零状态响应')

plt.xlim(0,10)
plt.ylim(-0.05,0.05)
plt.show()