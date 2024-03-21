# Due centralini, tra di loro indipendenti, ricevono nell’unità di tempo un numero di telefonate X e Y
# aventi legge di Poisson di parametri rispettivamente λ e μ.
# a) Qual è la probabilità che nell’unità di tempo i due centralini ricevano insieme non più di tre
# telefonate, supponendo λ = 2 e μ = 4?
# b) Calcolare la legge condizionale di X dato X+Y=n. Si tratta di una densità nota? Quanto vale la
# media di questa legge condizionale?
# c) Supponendo λ = 2 e μ = 4 e sapendo che nell’unità di tempo i due centralini hanno ricevuto
# complessivamente 8 telefonate, qual è la probabilità che il primo ne abbia ricevute 3?

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

a = poisson.pmf(0,2) + poisson.pmf(1,2) + poisson.pmf(2,2) + poisson.pmf(3,2)
print(a)
