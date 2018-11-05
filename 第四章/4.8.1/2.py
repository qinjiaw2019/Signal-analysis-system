from sympy import *
from sympy.abc import s,t

f = (s-2)/(s**4+3*s**3+3*s**2+s)
F_s = inverse_laplace_transform(f,s,t)
print(F_s)
