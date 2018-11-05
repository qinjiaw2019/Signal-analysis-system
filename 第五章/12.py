import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import *
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

a = [1,-5,6]
b = [1,0,3]
system = (b,a,1.0)
n = np.arange(0,30)
t1,h = dimpulse(system,t=np.asarray(n))
plt.stem(n,h[0])

plt.show()