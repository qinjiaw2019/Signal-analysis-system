import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(0,2,0.001)
a = 2
y = np.sin(2*np.pi*t)
y1 = np.sin(2*a*np.pi*t)
y2 = np.sin(2*np.pi*t/a)
plt.subplot(311)
plt.plot(t,y)
plt.axhline(0,0,2)
plt.title('尺度变换')

plt.subplot(312)
plt.plot(t,y1)
plt.axhline(0,0,2)

plt.subplot(313)
plt.plot(t,y2)
plt.xlabel('t')
plt.axhline(0,0,2)

plt.show()