import matplotlib.pyplot as plt
import numpy as np
labels=["ali","hasan","reza"]
y1=[5,2,10]
y2=[5,7,1]
fig,ax=plt.subplots(2,1,figsize=(6,6))
#plt.subplot(2,1,1)
ax[0].bar(labels,y1,label="teh")
ax[0].bar(labels,y2,bottom=y1,label="esf")
#plt.subplot(2,1,2)
x=np.arange(len(labels))
w=0.2
ax[1].bar(x-w/2,y1,width=w,label="teh")
ax[1].bar(x+w/2,y2,width=w,label="esfe")
ax[1].set_xticks(x)
ax[1].set_xticklabels(labels)
plt.legend()
plt.show()

