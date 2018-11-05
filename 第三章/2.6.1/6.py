from sympy import *
from sympy import plot_implicit,integrate
import numpy as np
from sympy.abc import t,v
#
F = fourier_transform(exp(-2*abs(t)),t,v)
plot(exp(-2*abs(t)),xlim=[-3,3],title='exp(-2*abs(t))')
plot(F,xlim=[-6,6],title='4/(4+w^2)')