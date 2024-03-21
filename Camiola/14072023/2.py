# Il punteggio ottenuto dagli studenti in un compito in classe segue una legge
# normale con distribuzione normale di μ = 7.5 e σ2 = 4.
# A. Qual é la probabilità che uno studente prenda un voto inferiore a 4?
# B. Se al compito partecipano 30 studenti, qual è la probabilità che ci sia un voto
# inferiore a 4?

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, binom
media = 7.5
std = 2
xx = np.linspace(0,15,100)
yy = norm.pdf(xx,media,std)

inf_4 = norm.cdf(4,media,std)
print("probabilità voto inferiore a 4: "+str(inf_4))

print(norm.pdf(4,media,std))

# B(30,p)
print(binom.pmf(1,30,inf_4))

# plt.plot(xx,yy)
# plt.show()