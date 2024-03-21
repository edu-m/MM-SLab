import numpy as np
from scipy.stats import binom

X = np.loadtxt("Dataset_motore.dat")
print(X)

mu0 = 2000
D = X - mu0
alpha = 0.05
n = X.size
print(D)
differenze_positive = D > 0
# print(differenze_positive)
num_diff_pos = np.sum(differenze_positive.astype(int))
print(num_diff_pos)

k = range(num_diff_pos, n+1)
bin = binom.pmf(k, n, 1/2)
pvalue = 2 * np.sum(bin)
# print(pvalue)
if pvalue <= alpha:
    print("mu != mu0")
else:
    print("mu = mu0")