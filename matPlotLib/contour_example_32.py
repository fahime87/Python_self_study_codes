import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,10,0.5)
y=np.arange(-10,10,0.5)
X,Y=np.meshgrid(x,y)
r=np.sqrt(X**2+Y**2)
Z=np.sin(r)
###first solution
#fig,ax=plt.subplots()
#cs=ax.contourf(X,Y,Z)
#fig.colorbar(cs)
#######################
fig=plt.figure()
ax=plt.axes(projection="3d")
#fig,ax=plt.subplots(subplot_kw={"projection":"3d"})##second syntax
#ax.plot_surface(X,Y,Z)
#ax.scatter3D(X,Y,Z)
ax.plot_wireframe(X,Z,Y)
plt.show()
