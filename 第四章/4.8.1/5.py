from scipy.signal import residue
b = [0,0,0,1,-2] #分子系数
a = [1,3,3,1,0] #分母系数
r,p,k = residue(b,a)
print(r,p,k)