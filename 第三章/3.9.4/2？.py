import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

T = 0.0625
f = 8
n = np.arange(0,5,1)
xs = np.cos(2*np.pi*f*n)
t = np.linspace(-0.5,500,1.5)
print(t[:,np.ones(len(n))])
# ya = np.sinc((1/T) * t[:,np.ones(len(n))]-(1/T)*n[:,np.ones[len(t)]])*xs

plt.show()
