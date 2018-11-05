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
    return x,n

ns = -2
nf = 7
np = 0
x,n= stepseq(np,ns,nf)

plt.stem(n,x)
plt.show()