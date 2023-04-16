import matplotlib.pyplot as plt
import numpy as np


x=np.arange(-2,2,0.1)
y=np.arange(-2,2,0.1)
X,Y=np.meshgrid(x,y)
Z=np.exp(-X**2-Y**2)
fig,ax=plt.subplots()
cs=ax.contourf(X,Y,Z)
#ax.clabel(cs,inline=1,fontsize=10)
fig.colorbar(cs)
plt.show()

