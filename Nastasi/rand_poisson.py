import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def randexp(lam):
    x = np.random.rand()
    return -np.log(x) / lam

def randpoisson(lam):
    eta_acc = 0
    k = 0
    while eta_acc <= 1:
        eta_acc = eta_acc + randexp(lam)
        k = k+1
    return k-1

lam = 3
N = 2000
X = np.zeros(N)
F = np.zeros(15)
for i in range(N):
    r = randpoisson(lam)
    X[i] = r
    F[int(X[i])] = F[int(X[i])]+1
F = F/N

x = np.arange(15)
y_t = poisson.pmf(x,lam)
plt.bar(x-0.5,y_t,0.5,label="teorico")
plt.bar(x,F,0.5,label="calcolato")
plt.legend()
plt.show()