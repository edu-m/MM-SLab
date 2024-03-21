# Da una rilevazione risulta che il numero di incidenti 
# sul lavoro avvenuti in una azienda in un mese è una variabile distribuita 
# secondo Poisson con valor medio 1,5. Calcolare 
# a) La probabilità che in un mese non ci siano incidenti. 
# b) La probabilità che in un mese ci siano più di 2 incidenti. 
# c) Il numero più probabile di incidenti.

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

l = 1.5

a = poisson.pmf(0,l)
print(a)

b = 1 - poisson.cdf(2,l)
print(b)
