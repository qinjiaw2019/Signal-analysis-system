import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

n = np.arange(0,10)
w0 = np.pi/5
w1 = np.pi/4
x = np.sin(n*w0+w1)

plt.stem(n,x)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('正弦型序列')

plt.show()