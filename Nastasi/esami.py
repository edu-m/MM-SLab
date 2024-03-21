import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

media = 24
std = 4

sp = np.linspace(0.,50.,100)
a = norm.pdf(sp,media,std)
voto_piudi27 = norm.cdf(27,media,std)
voto_menodi22 = norm.cdf(22,media,std)
voto_minoredi23 = norm.cdf(23,media,std)
voto_minoredi25 = norm.cdf(25,media,std)
votocompreso = voto_minoredi25 - voto_minoredi23
votominimo_70 = media + std*norm.ppf(0.3)
votomassimo_90 = media - std*norm.ppf(0.1)

print("numero di studenti che hanno riportato un voto superiore a 27: "+str(1-voto_piudi27))
print("la probabilità che uno studente abbia riportato un voto inferiore a 22: "+str(voto_menodi22))
print("la probabilità che uno studente abbia riportato un voto compreso tra 23 e 25: "+str(votocompreso))
print("il voto minimo riportato dal 70% degli studenti: "+str(round(votominimo_70)))
print("il voto massimo non superato dal 90% degli studenti: "+str(round(votomassimo_90)))

plt.plot(sp,a)
plt.show()