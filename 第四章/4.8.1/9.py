import numpy as np
from pylab import mpl
from scipy.signal import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


b = [1,2,5,8,4] #分母多项式系数
a = [0,1,-2,2,0] #分子多项式系数
r1 = np.roots(a)
r2 = np.roots(b)

z1, p1, k1 = tf2zpk(b,a)

print(r1)
print(r2)

fig, ax = plt.subplots()

for i in p1:
    ax.plot(np.real(i),np.imag(i), 'bx')    #pole before quantization

for i in z1:
    ax.plot(np.real(i),np.imag(i),'bo')     #zero before quantization
plt.axhline(0,-1,1,linestyle='--')
plt.axvline(0,-2,2,linestyle='--')
plt.show()