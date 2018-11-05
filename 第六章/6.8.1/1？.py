from sympy import S
from sympy import *
from sympy.concrete.gosper import gosper_sum
from sympy.functions import factorial
from sympy.abc import n,z

f1 = 3**n*z**(-n)
F1_z = gosper_sum(f1,(n,0,S.Infinity))
f2 = cos((pi/2)**n)
F2_z = gosper_sum(f1,(n,0,S.Infinity))

print(F1_z)
print(F2_z)