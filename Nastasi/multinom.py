import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multinomial

a = multinomial.pmf([0,1,0,0,0,3], n=4, p=[1/6,1/6,1/6,1/6,1/6,1/6])
print(a)