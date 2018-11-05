import matplotlib.pyplot as plt
from scipy.signal import *
import numpy as nps

def stepseq(n0,n1,n2):
    import numpy as np
    n = np.arange(n1,n2+1)
    x = np.zeros(len(n))
    j = 0
    for i in n:
        if i>=0:
            x[j] = 1
        j+=1
    return np.array(x),n

n = nps.arange(0,20)

x1 = n * (stepseq(0,0,20)[0]-stepseq(8,0,20)[0])
print(x1)
# x2 = 10*nps.exp(-0.3*(n-10))*(stepseq(10,0,20)[0]-stepseq(16,0,20)[0])
# x = x1 -x2
# E = nps.sum((nps.abs(x)**2))

# print('E=',E)