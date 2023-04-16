import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,100,1000)
y1=np.sin(x)
y2=np.exp(x)
fig,ax=plt.subplots()
ax.plot(x,y1,color="green",label="sin")
ax.set_xlabel("X")
ax.set_ylabel("Sin",color="green")


ax2=ax.twinx()
ax2.plot(x,y2,color="red",label="Exp")
ax2.set_ylabel("Exp",color="red")

fig.tight_layout()
plt.legend()
plt.show()
