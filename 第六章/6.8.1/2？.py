from sympy import S
from sympy import *
from sympy.concrete.gosper import gosper_sum,gosper_normal
from sympy.functions import factorial
from sympy.abc import z,n

f1 = z**2/((z-1)*(z-0.5))
F1_z = gosper_normal(f1,(z,0,S.Infinity))


print(F1_z)
