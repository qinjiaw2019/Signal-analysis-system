from sympy import *
from sympy.abc import t,f

F = inverse_fourier_transform(1/(1+(2*pi*f)**2),f,t)
print(F)