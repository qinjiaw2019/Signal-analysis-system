import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

n = np.arange(0,10)
a = 1
x = n * a
plt.stem(n,x)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('单位斜变序列x(n)')

plt.show()