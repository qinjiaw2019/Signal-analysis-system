from sympy import *
import numpy as np
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(-1,1,0.02)
t = symbols('t')
g = t**2
d = diff(g,t)

plot(g,xlim=[-6.1,6.1],ylim=[0,40],ylabel='g(t)',title='微分')
plot(d,xlim=[-6.1,6.1],ylim=[-15,15],ylabel='d(t)',xlabel='t',title='2t')