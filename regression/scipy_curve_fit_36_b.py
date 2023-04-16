import scipy.optimize as op
import numpy as np
import matplotlib.pyplot as plt
def f(x,A,w,theta):
    return A*np.sin(w*x+theta)
A=3
w=200
theta=np.pi*0.2
print(theta)
x=np.arange(-5,5,0.25)
y=f(x,A,w,theta)+np.random.normal(size=(40))

popt,pcov=op.curve_fit(f,x,y)
print(popt)

A_pre,w_pre,theta_pre=popt

x0=np.arange(-5,5,0.3)
y_pred=f(x0,A_pre,w_pre,theta_pre)


plt.scatter(x,y,label="data")
plt.plot(x0,y_pred,color="red",label="pre func")
plt.legend()
plt.show()
