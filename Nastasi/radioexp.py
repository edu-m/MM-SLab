import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon

l = 1/8
prob_m10 = 1 - expon.cdf(10,0,1/l)
xx = np.linspace(0,150,100)
yy = expon.pdf(xx,0,1/l)
print(prob_m10)
plt.plot(xx,yy)
plt.show()
