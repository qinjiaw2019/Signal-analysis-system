import matplotlib.pyplot as plt
from scipy.signal import *
import numpy as nps
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def stepseq(n0,n1,n2):
    import numpy as np
    n = np.arange(n1,n2+1)
    x = np.zeros(len(n))
    j = 0
    for i in n:
        if i>=0:
            x[j] = 1
        j+=1
    return np.array(x)

nf = 30
np = 0
ns = 0
n = nps.arange(0,31)
b = [1]
a = [1,-0.9]
x = 0.05*stepseq(np,ns,nf)
Y = [0]

tout,y = dlsim((b,a,1.0),x,nps.asarray(n))

plt.subplot(211)
plt.stem(n,x)
plt.ylabel('x(n)')
plt.title('输入序列')


plt.subplot(212)
plt.stem(n,y)
plt.ylabel('y(n)')
plt.title('输出序列')

plt.show()

