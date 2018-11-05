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
t = np.arange(-2,2,T)
f = stepfun(t,-1)-stepfun(t,1)
plt.plot(t,f)

plt.hlines(0,-2,2)
plt.vlines(0,-0.2,1.2)

plt.title('门函数')
plt.show()