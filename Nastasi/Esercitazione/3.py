import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, t
X = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
Y = np.array([10, 11, 10.5, 12, 10, 12, 11, 13])
alpha = 0.05
n = X.size
x_bar = np.mean(X)
y_bar = np.mean(Y)
T = t.ppf(1-alpha/2,n-2)
sig_xy = np.sum((X-x_bar)*(Y-y_bar))/n
sig_x_2 = np.var(X)
sig_y_2 = np.var(Y)
b0 = y_bar - sig_xy / sig_x_2 * x_bar
b1 = sig_xy / sig_x_2
y_hat = b0 + b1*X
sse = np.sum((Y-y_hat)**2)
s = np.sqrt(sse/(n-2))
intb0 = s*np.sqrt(1/n+x_bar**2/(n*sig_x_2))*T
intb1 = s/np.sqrt(sig_x_2)*np.sqrt(n)*T
infb0 = b0 - intb0
supb0 = b0 + intb0
infb1 = b1 - intb1
supb1 = b1 + intb1
print(infb0,supb0)
print(infb1,supb1)
xx = np.linspace(np.min(X),np.max(X)+5,100)
yy = b0 + b1*xx
plt.plot(X,Y,"*")
plt.plot(xx,yy)
plt.show()
# print(np.sum(X-x_bar))

pearson = pearsonr(X,Y)
print(pearson)

x0 = 2022
previsione2022 = b0 + b1*(x0)
print(previsione2022)


func = b0+b1*x0
intervallo = np.sqrt(1 + 1/n + (x0-x_bar)**2 / (n*sig_x_2)) * T
sup = func + intervallo
inf = func - intervallo
print(sup,inf)