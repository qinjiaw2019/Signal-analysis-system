from scipy.signal import *

B = [0,-2]
A = [-4,-3,-1]
k = [1]

b,a = zpk2tf(B,A,k)

print('b=',b)
print('a=',a)