from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def du_dx(u,x):
    return[u[1],np.cos(2*x)-2*u[1]-2*u[0]]

x=np.linspace(0,10,100)

u0=[0,0]
u=odeint(du_dx,u0,x)
plt.plot(x,u[:,0],color="red")
print(u)
plt.show()
