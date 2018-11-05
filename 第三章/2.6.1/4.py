import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from sympy import *
from sympy.abc import t,f

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

ft = exp(-0.1*t)*Heaviside(t)
F = fourier_transform(ft,t,f)
plot(ft,ylabel='f(t)')
# plot(abs(F),ylim=[0,10],xlim=[-2,2],ylabel='幅频')
# plot(atan(im(F)/re(F)),ylim=[-2,2],xlim=[-2,2],ylabel='相频')
