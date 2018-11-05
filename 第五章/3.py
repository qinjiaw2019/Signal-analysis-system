import matplotlib.pyplot as plt

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def rectseq(n0,n1,n2,N):
    import numpy as np
    n = np.arange(n1,n2+1)
    x = np.zeros(len(n))
    j = 0
    for i in n:
        if i>=0 and i<=N-1:
            x[j] = 1
        j+=1

    return x,n
ns = -2
nf = 8
np = 0
np1 = 4
N = 4
x,n= rectseq(np,ns,nf,N)

plt.stem(n,x)
plt.ylabel('R4(n)')
plt.xlabel('n')
plt.title('矩阵序列R4(n)')
plt.show()