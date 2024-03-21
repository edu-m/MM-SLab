import matplotlib.pyplot as plt
import numpy as np
import math

data = np.array([1.01,1.02,1.02,1.03,2])
w = 0.01
n = math.ceil((data.max() - data.min())/w)
plt.hist(data, bins = n)
plt.show()