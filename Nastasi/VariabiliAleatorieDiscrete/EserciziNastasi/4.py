# Si lancia un dado equilibrato finché non esca un numero dispari.
# a) Qual è la probabilità che ciò avvenga al quarto tentativo?
# b) Quanti tentativi sono necessari affinché si abbia una probabilità maggiore del 95% che esca un
# numero dispari esattamente al tentativo successivo?
# c) Sapendo che nei primi 4 lanci non si è avuto un numero dispari, qual è la probabilità che si
# abbia un numero dispari per la prima volta al settimo tentativo?

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, geom

# P(X = 4)
print(1/2 * (1 - 1/2)**3)

a = geom.ppf(0.95,1/2)
print(a)
# print("1/2 ^ x < 0.05 -> x > 4")

# P P (D)

print(1/2 * (1 - 1/2)**2)