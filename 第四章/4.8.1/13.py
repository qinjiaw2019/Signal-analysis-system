from scipy.signal import *

b = [0,1,2,0]
a = [1,8,19,12]
B,A,k = tf2zpk(b,a)

print('B=',B)
print('A=',A)
print('k=',k)