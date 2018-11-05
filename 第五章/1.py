import matplotlib.pyplot as plt
from scipy.signal import *
import numpy as nps

def impseq(n0,n1,n2):
    import numpy as np
    # n = np.arange(n1,n2)
    # return [(n-n0)==0]
    n = n2 - n0 + 1
    k = []
    x = np.zeros(n2+1-n1)
    j = 0
    for i in np.arange(n1,n2+1):
        k.append(i)
        if i==n0:
            x[j] = 1
        j=j+1

    return x,k
ns = -2
nf = 7
np = 0
x,n= impseq(np,ns,nf)

plt.stem(n,x)
plt.xlabel('n')
plt.ylabel('x(n)')

plt.show()