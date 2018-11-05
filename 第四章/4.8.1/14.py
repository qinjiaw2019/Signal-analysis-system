from scipy.signal import *
b = [0,1,2,0]
a = [1,8,19,12]
r,p,k= residue(b,a)

print('r=',r)
print('p=',p)
print('k=',k)