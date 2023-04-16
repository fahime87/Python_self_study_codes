import scipy.optimize as op
import numpy as np
import matplotlib.pyplot as plt
def f(x,a,b,c):
    d=np.power(x,b,dtype = complex)
    return x*a+c
a=3
b=2
c=2.5
x=np.arange(-5,5,0.25)
y=f(x,a,b,c)+np.random.normal(size=(40))

popt=op.curve_fit(f,x,y)
print(popt)


