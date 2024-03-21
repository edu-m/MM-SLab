# Un negoziante ha constatato che è richiesta la vendita 
# di un certo oggetto mediamente una volta al giorno. 
# Quanti di questi oggetti deve tenere in negozio per essere sicuro, 
# almeno con una probabilità del 95% di soddisfare le richieste della 
# clientela per un periodo di una settimana (6 giorni) ? 

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson
l = 6

i = 0
while poisson.cdf(i,6) < 0.95:
    i+=1
b = poisson.cdf(i,6)
print("per k="+str(i)+" la probabilità che la clientela sia soddisfatta è "+str(b))