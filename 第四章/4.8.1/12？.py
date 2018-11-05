from control import *

a = [1,2,5,8,4]
b = [0,1,-2,2,0]

sys = tf(b,a)
bode(sys)