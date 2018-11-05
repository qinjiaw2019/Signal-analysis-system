from scipy.signal import lti,step2,impulse2
import matplotlib.pyplot as plt
from pylab import mpl


b = [1]
a = [1,1]
sys = lti(b,a)
t,y=step2(sys)
plt.plot(t,y)

plt.hlines(0,0,7)
plt.vlines(0,0,1)

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.xlabel('时间(t)')
plt.ylabel('y(t)')
plt.title('单位阶跃响应')

plt.show()