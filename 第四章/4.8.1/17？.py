from scipy.signal import *
import numpy as np
from control import *

b1 = [1,4,3]
a1 = [1,5,1]
b2 = [2,6]
a2 = [1,1]

b,a = feedback(b1,a1,b2,a2)

print('b=',b)
print('a=',a)