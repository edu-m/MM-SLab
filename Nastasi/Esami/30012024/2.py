# Si ritiene che i grammi di solidi rimossi da un materiale (y) siano correlati al tempo di asciugatura
# (x) espresso in ore. Da uno studio sperimentale si ottengono le 10 misurazioni riportate nella seguente
# tabella.
# x 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0
# y 4.3 1.5 1.8 4.9 4.2 4.8 5.8 6.2 7.0 7.9
# 1. Si determinino i coefficienti della retta di regressione e i loro intervalli di confidenza al 95%. Si
# calcoli il coefficiente di determinazione.
# 2. Si rappresentino i dati e la retta di regressione in uno stesso grafico.
# 3. Si stimi la quantita in grammi di solidi rimossi a 4.25 ore.
# 4. Si effettui il test di indipendenza con un livello di significativita α = 0.05 commentandone l’esito.

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

x = np.array([2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
y = np.array([4.3, 1.5, 1.8, 4.9, 4.2, 4.8, 5.8, 6.2, 7.0, 7.9])

n = x.size

x_bar = x.mean()
y_bar = y.mean()

sig_xy = np.sum((x-x_bar)*(y-y_bar))/n
print(sig_xy)

sig_x_2 = np.var(x)
print(sig_x_2)

b0 = y_bar - sig_xy/sig_x_2*x_bar
b1 = sig_xy / sig_x_2

xx = np.linspace(np.min(x),np.max(x),100)
yy = b0 + b1*xx

plt.plot(x,y,"*")
plt.plot(xx,yy)
plt.show()

print(b0+b1*4.25)

alpha = 0.05
y_hat = b0 + b1*x
r = y - y_hat
s2 = np.sum(r**2)/(n-2)
T = t.ppf(1-alpha/2,n-2)
b0inf = b0 - np.sqrt(s2)*np.sqrt(1/n+x_bar**2/(n*sig_x_2))*T
b0sup = b0 + np.sqrt(s2)*np.sqrt(1/n+x_bar**2/(n*sig_x_2))*T
print("intervallo b0 "+ str([b0inf,b0sup]))
b1inf = b1 - np.sqrt(s2) / (np.sqrt(sig_x_2) * np.sqrt(n)) * T
b1sup = b1 + np.sqrt(s2) / (np.sqrt(sig_x_2) * np.sqrt(n)) * T
print("intervallo b1 "+ str([b1inf,b1sup]))

# ipotesi nulla: b1 = 0
# ipotesi alternativa: b1 != 0

alpha = 0.05
T1 = np.sqrt(n)*(b1/np.sqrt(s2))*np.sqrt(sig_x_2)
if(np.abs(T1) >= T):
    print("ipotesi alternativa accettata")
else:
    print("ipotesi nulla accettata")

sig_y_2 = np.var(y)
print(sig_xy**2)
print(sig_x_2)
print(sig_y_2)
r2 = sig_xy**2 / (sig_x_2*sig_y_2)
print(r2)