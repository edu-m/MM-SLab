import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2,poisson

X = np.array([584,398,165,35,15])
s = np.sum(X)
p = X/s
m = 5
n = X.size
print(p)
Xn = X*np.array([0,1,2,3,4])
lam = np.sum(Xn)/s

p0 = np.zeros(m)
for i in range(m-1):
    p0[i] = poisson.pmf(i,lam)
p0[4] = 1-np.sum(p0)
print(np.sum(p0))

T = s*np.sum((p-p0)**2/p0)
print(T)
alpha = 0.05

chi = chi2.ppf(1-alpha,m-2)
print(chi)
if T > chi:
    print("Ipotesi alternativa")
else:
    print("Ipotesi nulla")