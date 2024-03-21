# E noto che il numero di pezzi guasti fabbricati in una giornata di lavoro di una catena di produzione
# A segue una distribuzione di Poisson di media 2.
#
# 1. Qual e la probabilita che in un giorno siano stati prodotti esattamente 3 pezzi guasti?
# 2. Qual e la probabilita che in un giorno siano stati prodotti tra 2 e 5 pezzi guasti (estremi inclusi)?
# Si mette in opera una nuova catena di produzione B. E noto che il numero di pezzi guasti fabbricati
# in una giornata di lavoro mediante B segue una distribuzione di Poisson di media 1.5.
# 3. Si trovi la legge della variabile aleatoria che conta complessivemente il numero di pezzi guasti
# prodotti (cioe provenienti indifferentemente da A o da B) e si calcoli la sua media e la sua
# varianza.
# 4. Qual e la probabilita che in un giorno siano stati prodotti complessivamente un numero di pezzi
# guasti compreso tra 3 e 6 (estremi inclusi)?

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# punto 1
l = 2
a = poisson.pmf(3,l)
print(a)

# punto 2
b = poisson.cdf(5,l) - poisson.cdf(1,l)
print(b)

# punto 3
print("X+Y ~ P(λ+μ) -> X+Y ~ P(1.5+2) -> X+Y ~ P(3.5). Media = 3.5 Varianza = 3.5")

# punto 4
m = 1.5
d = poisson.cdf(6,m+l) - poisson.cdf(2,m+l)
print(d)