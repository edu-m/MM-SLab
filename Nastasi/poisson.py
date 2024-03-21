import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

sp = np.arange(0,15)
a = poisson.pmf(sp, 0.61)
print(a)
plt.bar(sp,a)
plt.show()
