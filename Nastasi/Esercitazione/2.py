import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

X = np.array([4.65, 4.7, 4.75, 4.77, 4.8, 4.95, 5, 4.75, 4.54, 4.66])
n = X.size
alpha = 0.01
media = np.mean(X)
std = np.std(X)
T = t.ppf(1-alpha/2,n-1)
inf = media - std/np.sqrt(n)*T
sup = media + std/np.sqrt(n)*T
print([inf,sup])

# plt.boxplot(X)
# plt.show()
mu = 4.7
alpha = 0.05
T = t.ppf(1-alpha,n-1)
T0 = (media - mu)/std*np.sqrt(n)
if T0 > T:
    print("ipotesi alternativa accettata")
else:
    print("ipotesi nulla accettata")