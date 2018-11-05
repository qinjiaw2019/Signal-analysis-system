import numpy as np
from pylab import mpl
from scipy.signal import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


b = [1,2,5,8,4] #分母多项式系数
a = [0,1,-2,2,0] #分子多项式系数
# w = logspace(-1,1)
# w = np.linspace(0,5,200)



w,h = freqs(b,a,worN=np.logspace(-1,1)) #系统频应
Hmag = abs(h) #振幅特性
Hpah = np.angle(h)*180/np.pi #相位特性
plt.subplot(211) #做振幅图
plt.plot(w,Hmag)
plt.title('H(s)频响')
plt.ylabel('系统振幅')

plt.subplot(212)
plt.plot(w,Hpah)
plt.xlabel('频率')
plt.ylabel('系统相位')

plt.show()