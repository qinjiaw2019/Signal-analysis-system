import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

#序列位移扩展函数
def seqshift(x,nx,k):
    y = x
    ny = nx + k
    return y,ny

#序列相乘
def seqmult(x1,n1,x2,n2):
    n = np.arange(min(min(n1),min(n2)),max(max(n1),max(n2)))
    y1 = np.zeros(len(n))
    y2 = y1


x = [0.5,1.5,1,-0.5]
n0 = np.arange(-1,2)
a = 2
x1,n1 = seqshift(x,n0,2) #移位
ym1,n = seqmult(x1,n1,x,n0) #序列相乘


plt.show()