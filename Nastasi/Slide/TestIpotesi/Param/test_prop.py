import numpy as np
from scipy.stats import norm

# H0 : p = p0
# H1 : p < p0

p0 = 0.05
alpha = 0.05
n = 200
prop = 4/n

Z0 = (prop - p0) / np.sqrt(p0*(1-p0)) * np.sqrt(n)
phi = norm.ppf(alpha)
print(Z0)

if Z0 < phi:
    print("Ipotesi alternativa")
else:
    print("Ipotesi nulla")

p_star = 0.03
beta = 0.1

num = (norm.ppf(beta)*np.sqrt(p_star*(1-p_star))+norm.ppf(alpha)*np.sqrt(p0*(1-p0)))/(p0-p_star)
num = num**2

print(num)