# Si supponga che tre negozi della stessa tipologia attraggano rispettivamente il 20% della clientela, il
# 45% e il 35%. Scegliendo a caso 6 clienti, qual è la probabilità che 2 vadano nel primo negozio, 1 nel
# secondo e 3 nel terzo? Qual è la probabilità che nessun cliente vada nel primo negozio?

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multinomial, binom

# 0.2, 0.45, 0.35

print(1/5**2)

a = multinomial.pmf([2,1,3],6,[0.2,0.45,0.35])
print(a)

b = 0
for i in range(1,6):
    b += binom.pmf(i,6,0.2)
print(1 - b)