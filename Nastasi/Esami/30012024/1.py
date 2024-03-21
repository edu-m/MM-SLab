import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon

# Il tempo di vita di un dispositivo meccanico sottoposto a vibrazioni durante un test segue una
# distribuzione esponenziale con media 400 ore.
# 1. Qual `e la probabilit`a che il dispositivo fallisca il test in meno di 100 ore?
# 2. Qual `e la probabilit`a che il dispositivo operi per pi`u di 500 ore prima di rompersi?
# 3. Sapendo che il dispositivo ha operato per 400 ore senza fallire il test, qual `e la probabilit`a che
# fallisca nelle prossime 100 ore?
# 4. Quante ore di funzionamento sono necessarie per affermare che il dispositivo fallisca il test con
# probabilit`a superiore al 95%?

media = 400

a = expon.cdf(100,0,media)
print(a)

b = 1 - expon.cdf(500,0,media)
print(b)

c = expon.cdf(100,0,media)
print(c)

d = expon.ppf(0.95,0,media)
print(d)

d1 = expon.cdf(d,0,media)
print(d1)

xx = np.linspace(0,2500,100)
yy = expon.pdf(xx,0,media)

plt.plot(xx,yy)
plt.show()

