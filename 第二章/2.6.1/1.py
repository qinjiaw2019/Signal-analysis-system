from scipy.signal import lti,impulse2
import matplotlib.pyplot as plt
from pylab import mpl
import  numpy as np
a = [0,1,0]
b = [1,5,6]

sys = lti(a,b) #以分子分母的最高次幂降序的系数构建传递函数
t,y = impulse2(sys)

plt.plot(t,y,'r',label="s1 Step",linewidth=0.5)

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.xlabel('时间(t)')
plt.ylabel('h(t)')
plt.title('例2.6-1的单位冲击响应')

plt.xlim(-0.2,4)#设置x轴的区间
plt.ylim(-0.2,1)#设置y轴的区间

plt.vlines(0,-0.2,1)#x=0
plt.hlines(0,-0.2,4)#y=0

plt.show()