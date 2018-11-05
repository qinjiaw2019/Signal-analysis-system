import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

n = np.arange(0,10)
a1 = 0.5
a2 = -0.5
a3 = 1.2
a4 = -1.2

x1 = a1**n
x2 = a2**n
x3 = a3**n
x4 = a4**n

plt.subplot(221)
plt.stem(n,x1)
plt.xlabel('n')
plt.ylabel('x1(n)')
plt.title('实数序列(0<a1<1)')

plt.subplot(222)
plt.stem(n,x2)
plt.xlabel('n')
plt.ylabel('x1(n)')
plt.title('实数序列(-1<a2<0)')

plt.subplot(223)
plt.stem(n,x3)
plt.xlabel('n')
plt.ylabel('x1(n)')
plt.title('实数序列(a3>1)')

plt.subplot(224)
plt.stem(n,x4)
plt.xlabel('n')
plt.ylabel('x1(n)')
plt.title('实数序列(a4<-1)')

plt.show()