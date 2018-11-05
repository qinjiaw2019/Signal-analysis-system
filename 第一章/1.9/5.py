import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

t = np.arange(0,3,0.01)
a = -3
b = 4
f = np.exp((a + 1j * b) * t)
plt.subplot(2,2,1)
plt.plot(t,np.real(f))
plt.title('实部')
plt.xlabel('时间t')
plt.ylabel('幅值f')
plt.grid(color='b' , linewidth='0.3' ,linestyle='--')

plt.subplot(2,2,2)
plt.plot(t,np.imag(f))
plt.title('虚部')
plt.xlabel('时间t')
plt.ylabel('幅值f')
plt.grid(color='b' , linewidth='0.3' ,linestyle='--')

plt.subplot(2,2,3)
plt.plot(t,np.abs(f))
plt.title('模')
plt.xlabel('时间t')
plt.ylabel('幅值f')
plt.grid(color='b' , linewidth='0.3' ,linestyle='--')

plt.subplot(2,2,4)
plt.plot(t,np.angle(f))
plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
plt.title('相角')
plt.xlabel('时间t')
plt.ylabel('幅值f')


plt.show()
