# La probabilità di contrarre una malattia rara è dello 0.03%. Qual è la probabilità che in una città
# dove vivono 20000 persone vi siano meno di 4 persone che contraggono la malattia? Costruire il
# grafico della densità e della funzione di ripartizione della distribuzione in esame

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

prob = 0.03 / 100
l = 20000 * prob
print(l)

a = poisson.cdf(3,l)
print(a)

sp = np.arange(0.,10.)
x = poisson.cdf(sp,l)
plt.bar(sp,x)
plt.show()