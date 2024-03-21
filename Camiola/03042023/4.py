import numpy as np
from scipy.stats import norm, t
import matplotlib.pyplot as plt

X = np.array([16.1, 13.9, 15.1, 17.5, 14.9, 15.8, 16.3])

alpha = 0.05
n = X.size
media = np.mean(X)
mu = 15
s = np.std(X)
T0 = (media - mu) / s * np.sqrt(n)
T = t.ppf(1-alpha/2,n-1)

if np.abs(T0) > T:
    print("Ipotesi alternativa accettata")
else:
    print("Ipotesi nulla accettata")

p = 2*(1-t.cdf(np.abs(T0),n-1))
print("pvalue: "+str(p))