import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y,x):
    return -0.3*y

y0=5
x=np.linspace(0,20,40)
y=odeint(f,y0,x)
plt.plot(x,y,label="f")
plt.show()
