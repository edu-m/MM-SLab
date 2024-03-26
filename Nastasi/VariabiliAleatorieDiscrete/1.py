import numpy as np
from scipy.stats import binom

p = 0.05

a = binom.pmf(1, 4, p)
print(a)

b = binom.cdf(2, 4, p)
print(b)