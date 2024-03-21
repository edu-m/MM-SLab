# Da rilevazioni statistiche si è valutato che una 
# persona su 100.000 è allergica ad un tipo di polline. In una popolazione 
# di 300.000 abitanti calcola la probabilità che: 
# a) nessuna persona sia allergica
# b) al massimo tre persone siano allergiche

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

l = 3

a = poisson.pmf(0,l)
print(a)

b = poisson.cdf(3,l)
print(b)