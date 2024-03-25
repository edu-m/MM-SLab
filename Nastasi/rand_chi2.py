from scipy.stats import norm, chi2
import matplotlib.pyplot as plt
import numpy as np

N = 2000000
X = np.random.rand(N)
media = 1
varianza = 2
xi1 = X[0:int(N/2)] # distribuzione uniforme
xi2 = X[int(N/2):N]

eta1 = np.sqrt(-2*np.log(xi1))*np.cos(2*np.pi*xi2) # distr normale
eta2 = np.sqrt(-2*np.log(xi1))*np.sin(2*np.pi*xi2)
Y = np.zeros(N)
Y[0:int(N/2)] = eta1
Y[int(N/2):N] = eta2
print(Y.size)
# distr = media + np.sqrt(varianza)*Y

xx = np.linspace(-2,2,1000)
yy = chi2.pdf(xx,1)
plt.plot(xx,yy)
# contiamo le occorrenze di ciascun numero
# in modo da trovare la probabilità
plt.hist(Y**2,bins=100,density=True)
plt.show()