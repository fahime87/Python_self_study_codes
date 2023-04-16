import matplotlib.pyplot as plt
import numpy as np
r=np.arange(0,2,0.01)
theta=2*np.pi*r
fig,ax=plt.subplots(subplot_kw={"projection":"polar"})
ax.scatter(theta,r,color="yellow")
ax.set_rticks([0,0.5,1,1.5,2])#the circle lines in nemoodar
plt.show()
