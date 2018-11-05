from sympy import *
from sympy.abc import s,t
import numpy as np

f = (s**3+5*s**2+9*s+7)/(s**2+3*s+2)
F_s = inverse_laplace_transform(f,s,t)
print(F_s)
