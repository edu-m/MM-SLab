import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon


# sp = np.linspace(0.,15.,100)
a = 1-expon.cdf(1,0,1)
print(a)
# b = 1-expon.cdf(3,0,1)

# p = a * b
# print(p)
# plt.plot(sp,z)
# plt.xlabel("ore")
# plt.ylabel("pr. rip.")
# plt.show()