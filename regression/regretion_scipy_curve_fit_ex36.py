from scipy.optimize import curve_fit
import numpy as np
def f(x,a,b):
    return(a*x+b)**2
a=2.8
b=3.5
x=np.arange(-5,5,40)
y=f(x,a,b)+0.2*np.random.normal(size=(40))

popt,pcov=curve_fit(f,x,y)
a,b=popt
print("a =",a,"  b=",b)
