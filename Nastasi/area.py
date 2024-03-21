import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform

l = uniform.cdf(2/pow(3,1/4),0,2)
print(1-l)
