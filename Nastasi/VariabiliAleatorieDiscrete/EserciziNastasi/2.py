# Da una rilevazione risulta che il numero di incidenti stradali che avvengono ad un determinato
# incrocio in un mese segue una distribuzione di Poisson con valor medio 1.5.
# a) Qual è la probabilità che in un mese non ci siano incidenti?
# b) Qual è la probabilità che in un mese ci siano più di due incidenti?

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

l = 1.5
a = poisson.pmf(0,1.5)*100
a = round(a*100)/100
print("Qual è la probabilità che in un mese non ci siano incidenti?: "+str(a)+"%")

b = (1 - poisson.cdf(2,1.5))*100
b = round(b*100)/100
print("Qual è la probabilità che in un mese ci siano più di due incidenti?: "+str(b)+"%")