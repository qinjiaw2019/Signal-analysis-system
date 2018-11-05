from sympy import *
import numpy as np
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(-1,1,0.2)
t = symbols('t')
f = t**2
y = integrate(f,t)


plot(f,xlim=[-6,6],ylim=[0,40],ylabel='f(t)',xlabel='t',title='积分')
plot(y,xlim=[-6,6],ylim=[-55,55],ylabel='y(t)',xlabel='t',title='1/3t^3')