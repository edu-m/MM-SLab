import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

media = 175
std = 9

sp = np.linspace(140.,210.,100)
a = norm.pdf(sp,media,std)
prob = norm.cdf(153,media,std)
prob = 1-norm.cdf(190,media,std)
print(prob)

plt.plot(sp,a)
plt.xlabel("statura")
plt.ylabel("prob.")
plt.show()