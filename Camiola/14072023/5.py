import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

X = np.array([0,1,2,3,4,5,6,7,8,9,10])
Y = np.array([19.5,22.1,24.3,25.7,26.1,28.5,30,32.1,32.7,32.7,35])

n = X.size
x_bar = X.mean()
y_bar = Y.mean()

sig_x_2 = np.var(X)
sig_y_2 = np.var(Y)
sig_xy = np.sum((X-x_bar)*(Y-y_bar))/n

b0 = y_bar - sig_xy/sig_x_2 * x_bar
b1 = sig_xy / sig_x_2

xx = np.linspace(np.min(X),np.max(X),100)
yy = b0 + b1 * xx
plt.plot(X,Y,"*")
plt.plot(xx,yy)
# plt.show()

alpha = 0.05
y_hat = b0 + b1 * X
r = Y - y_hat
s_2 = np.sum(r**2)/(n-2)
s = np.sqrt(s_2)
T = t.ppf(1-alpha/2,n-2)

b0int = s*np.sqrt(1/n+x_bar**2/(n*sig_x_2))*T
b1int = s/(np.sqrt(sig_x_2)*np.sqrt(n))*T

b0conf = [b0 - b0int, b0 + b0int]
b1conf = [b1 - b1int, b1 + b1int]
print(b0conf,b1conf)
print(b0+b1*11)

T0 = np.abs(np.sqrt(n)*b1/s*np.sqrt(sig_x_2))
print(T0)
if T0 >= T:
    print("ipotesi alternativa accettata")
else:
    print("ipotesi nulla accettata")

r2 = sig_xy**2 / (sig_x_2 * sig_y_2)
print(r2)