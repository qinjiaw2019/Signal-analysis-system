import numpy as np
import matplotlib.pyplot as plt
import signal  as sgl
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题



def wrap(t):
    if t > 0 :
       return 1
    else:
       return 0


T = 0.01
t = np.arange(-2,6,T)
plt.ylim(-0.2,1.2)
plt.xlim(-1,6)

def stepfun(t,t0):
    y = []
    for i in t:
        if i>=t0:
            y.append(1)
        else:
            y.append(0)
    return y
y = stepfun(t,0)
plt.plot(t,y)

plt.xlabel('时间t')
plt.ylabel('幅值f')
plt.title('单位阶跃信号')

plt.show()

