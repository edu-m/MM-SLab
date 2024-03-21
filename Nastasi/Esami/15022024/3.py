import numpy as np

# 1 -> 2, 1 -> 3
# 2 -> 1, 2 -> 3
# 3 -> 1, 3 -> 2

# p = 1/3 -> 1-p = 2/3
# | 0 | p |1-p| sum = 1
# |1-p| 0 | p | sum = 1
# | p |1-p| 0 | sum = 1

p = 1/3
P = np.array(
[[0,p,1-p],[1-p,0,p],[p,1-p,0]])

P2 = np.dot(P,P)
print(P2)

lam, V = np.linalg.eig(P.T)
print(lam)
print(V)
v = np.real(V[:,0])/np.sum(np.real(V[:,0]))
print(v)

n = 3
F = np.zeros(n)
j = np.random.randint(n)
N = 1000000
F[j] = 1
for i in range(N):
    j_multi = np.random.multinomial(1, P[j,:]) # 0 0 1, 0 1 0, 1 0 0
    j = np.nonzero(j_multi)[0][0]
    F[j] = F[j] + 1
vv = F/N
print(vv)

'''
pi_i*p_ij = pi_j*p_ji
pi_i = pi_j essendo la distribuzione uniforme
pi_i*p_ij = pi_i*p_ji divido tutto per pi_i
p_ij = p_ji
se devono essere equivalenti
pi(n)
p_ij = p_ji
2p = 1
p = 1/2
'''