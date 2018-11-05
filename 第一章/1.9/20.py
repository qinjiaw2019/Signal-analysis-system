from sympy import *
from sympy import plot_implicit,integrate
t = Symbol('t')
f= t**2
y = integrate(f,(t,-1,1))
print(y)