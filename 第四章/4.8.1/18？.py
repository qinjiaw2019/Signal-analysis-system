from scipy.signal import *
import matplotlib.pyplot as plt
from control import *
import numpy as np
b = [2,5,1]
a = [1,2,3]
sys = tf(b,a)

r,m = rlocus(sys)


print(len(r))
print(len(m))
plt.plot(m,r)
plt.xlim(-3,1)
plt.ylim(-1.5,1.5)

plt.show()

