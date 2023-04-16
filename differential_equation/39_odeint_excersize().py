from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def dv_dt(v,t):
    return 10*t

t=np.linspace(0,5,40)
v0=1
vt=odeint(dv_dt,v0,t)
plt.plot(t,vt)
plt.show()
