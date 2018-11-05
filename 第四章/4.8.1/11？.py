import numpy as np
from pylab import mpl
from scipy.signal import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


b = [1,2,5,8,4] #分母多项式系数
a = [0,1,-2,2,0] #分子多项式系数

w,h = freqs(b,a) #系统频应

print(w,h)
plt.subplot(211)
plt.plot(w,np.abs(h))
plt.xlim(0.01,10)
plt.ylim(0.01,100)

plt.subplot(212)
plt.plot(w,np.angle(h)*(-180)/np.pi)
plt.xlabel('f/(rad/s)')
plt.ylabel('相位')
plt.show()