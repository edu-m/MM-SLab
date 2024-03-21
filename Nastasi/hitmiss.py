import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

def fun(x):
    return np.exp(-x**2/2)/np.sqrt(2*np.pi)

a = 0.5
b = 2

x = np.linspace(-3,3,1000)
y = fun(x)
plt.plot(x,y)
plt.show()