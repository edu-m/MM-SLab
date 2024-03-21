import matplotlib.pyplot as plt
import numpy as np

def fun(x):
    return -3/4*x**2 + 3/2*x

def rigetto(a,b,M):
    while True:
        r1 = np.random.rand()
        r2 = np.random.rand()
        xi = a + r1*(b-a)
        eta = M*r2
        if eta <= fun(xi):
            return xi

a = 0
b = 2
M = 0.7499234771962044
xx = np.linspace(a,b,100)
yy = fun(xx)

# plt.plot(xx,yy)
# plt.show()

N = 100000
X = np.zeros(N)
for i in range(N):
    X[i] = rigetto(a,b,M)

plt.hist(X, bins=100, density=True)
plt.plot(xx,yy)
plt.show()