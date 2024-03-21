# Il contenuto di sodio (in milligrammi) di 30 scatole di cereali e riportato di seguito
# 131.15, 130.69, 130.91, 129.54, 129.64, 128.77, 130.72,
# 128.33, 128.24, 129.65, 130.14, 129.29, 128.71, 129.00, 129.39,
# 130.42, 129.53, 130.12, 129.78, 130.92, 131.15, 130.69, 130.91,
# 129.54, 129.64, 128.77, 130.72, 128.33, 128.24, 129.65.
# 1. Si calcoli la media campionaria, la deviazione standard e l’intervallo di confidenza per la media
# con livello di fiducia 0.01.
# 2. Rappresentare graficamente i dati mediante un istogramma e mediante un box-plot.
# 3. Si testi l’ipotesi che il contenuto medio di sodio sia di 130 mg utilizzando α = 0.05. Si calcoli il
# p-value del test precedente.
# 4. E possibile affermare che il contenuto di sodio e distribuito normalmente nelle scatole? Giusti-
# ficare la risposta.

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm, t, chi2

array = np.array([131.15, 130.69, 130.91, 129.54, 129.64, 128.77, 130.72,
128.33, 128.24, 129.65, 130.14, 129.29, 128.71, 129.00, 129.39,
130.42, 129.53, 130.12, 129.78, 130.92, 131.15, 130.69, 130.91,
129.54, 129.64, 128.77, 130.72, 128.33, 128.24, 129.65])

n = array.size
alpha = 0.01
media = np.mean(array)
print("media: "+str(media))
std = np.std(array,ddof=1)
print("dev. std: "+str(std))
T = t.ppf(1-alpha/2,n-1)

inferiore = media - std/np.sqrt(n)*T
superiore = media + std/np.sqrt(n)*T

print("superiore: "+str(superiore))
print("inferiore: "+str(inferiore))

# plt.hist(array,bins=20)
# plt.boxplot(array)
# plt.show()

# ipotesi nulla: mu = mu0
# ipotesi alternativa: mu > mu0
# punto 3
mu0 = 130
alpha = 0.05

t0 = (media - mu0)/std*np.sqrt(n)
print("t atteso: "+str(t0))
T = t.ppf(1-alpha,n-1)
print("t ottenuto: "+str(T))

p = 1-t.cdf(t0,n-1)
print("p-value: "+str(p))

if T > t0:
    print("ipotesi nulla accettata")
else:
    print("ipotesi alternativa accettata")

xx = np.linspace(120, 140, num=200)
yy = norm.pdf(xx, loc=media, scale=std)
plt.hist(array, density=True)
plt.plot(xx,yy)
plt.show()