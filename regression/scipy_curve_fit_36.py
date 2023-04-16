import scipy.optimize as op
import numpy as np
import matplotlib.pyplot as plt
def f(x,a,b):
    return (a*x+b)**2
a=1.7
b=0.92
x=np.arange(-5,5,0.25)
y=f(x,a,b)+3*np.random.normal(size=(40))

popt,pcov=op.curve_fit(f,x,y)

a_pre,b_pre=popt
print("predicted a=",a_pre," predicted b=",b_pre)

x0=np.arange(-5,5,0.3)
y_pred=f(x0,a_pre,b_pre)


plt.scatter(x,y,label="data")
plt.plot(x0,y_pred,color="red",label="pre func")
plt.legend()
plt.show()

