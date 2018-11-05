import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(-2,2,0.001) #信号的抽样点
N = 20
cO =0.5
f1 = cO * np.ones(len(t)) #计算抽样上的直流分量
for n in range(1,N+1): #偶次谐波为零
    f1 = f1 +np.cos(np.pi*n*t)*np.sinc(n/2)
plt.plot(t,f1)
plt.show()