import matplotlib.pyplot as plt
import numpy as np
r=np.random.rand(100)
theta=2*np.pi*r
color=theta
size=200*r**2
fig,ax=plt.subplots(subplot_kw={"projection":"polar"})
ax.scatter(theta,r,c=color,s=size)
plt.show()
