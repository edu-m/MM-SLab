import numpy as np
from scipy.stats import t

# mu_D = 0
# mu_D > 0

before = np.array([265,240,258,295,251,245,287,314,260,279,283,240,238,225,247])
after = np.array([229,231,227,240,238,241,234,256,247,239,246,218,219,226,233])

alpha = 0.05

n = before.size
D = before - after
D_bar = np.mean(D)
S = np.std(D,ddof=1)

T0 = D_bar / S * np.sqrt(n)
print(T0)
T = t.ppf(1-alpha,n-1)
print(T)

if T0 > T:
    print("Ipotesi alternativa")
else:
    print("Ipotesi nulla")