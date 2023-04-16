import numpy as np
import os
os.environ["OMP_NUM_THREADS"] = '1'
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

data=np.array([[120,50,1],[60,20,2],
               [145,65,1],[130,45,3],
               [5,15,2]])
si=[]
se=[]
for i in range(2,5):
    model=KMeans(n_clusters=i,max_iter=100,n_init=1)
    model.fit(data)
    se.append(model.inertia_)#index to find best number of clusters
    si.append(silhouette_score(data,model.labels_))#index to find best number of clusters
    print(model.labels_)
    print(model.cluster_centers_)
    print("_____________")

    
    
import matplotlib.pyplot as plt
plt.plot(range(2,5),se)
plt.ylabel("elbow")
plt.xlabel("cluster number")
plt.show()
  

plt.plot(range(2,5),si)
plt.ylabel("silhoutte")
plt.xlabel("cluster number")
plt.show()
