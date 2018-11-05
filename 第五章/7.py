import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

n = np.arange(0,10)
delta = -0.2
w1 = 0.7
x = np.exp((delta+1j*w1)*n)

plt.subplot(211)
plt.stem(n,np.real(x))
plt.ylabel('复指数序列的实部')
plt.title('复数序列')

plt.subplot(212)
plt.stem(n,np.imag(x))
plt.ylabel('复指数序列的虚部')
plt.xlabel('n')

plt.show()