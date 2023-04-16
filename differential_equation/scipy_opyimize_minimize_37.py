from scipy.optimize import minimize
import numpy as np
def f(x):
    return x+np.exp(-x)

min=minimize(f,-10,method="BFGS")
print(min)
