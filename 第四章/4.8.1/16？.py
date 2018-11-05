from scipy.signal import *
import numpy as np
r = [8/3,-1.5000,-1/6]
p = [-4.0000,-3.0000,-1.0000]

r,b,a = residue(r,p)

print('r=',r)
print('b=',b)
print('a=',a)