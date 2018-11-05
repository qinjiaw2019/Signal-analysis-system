from scipy.signal import residue
b = [1,5,9,7] #分子系数
a = [0,1,3,2] #分母系数

r,p,k = residue(b,a)
print(r,p,k)

