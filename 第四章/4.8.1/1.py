from sympy import *
from sympy.abc import t,s
import numpy as np

f = exp(-3*t)*sin(2*t)*Heaviside(t)
F_s = laplace_transform(f,t,s)
print(F_s)
