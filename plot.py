import matplotlib.pyplot as plt
import numpy as np
import math

from scipy.special import gamma

x = np.linspace(0, 10, 1000)

plt.plot(x, x, 'r', label='$n$') 
plt.plot(x, 2 ** x, 'g', label='$2^n$')
plt.plot(x, x * np.log(x), 'b', label='$n\lg n$')

plt.legend()
plt.show()
