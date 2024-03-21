import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

a = binom.pmf(2, 4, 1/6)
print(a)

# S S F F
# S F S F
# ...