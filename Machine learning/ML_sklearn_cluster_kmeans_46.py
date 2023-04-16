import numpy as np
import os
os.environ["OMP_NUM_THREADS"] = '1'
from sklearn.cluster import KMeans

data=np.array([[15],[15],[16],[19],[19],[20],[20],[21],
[22],[28],[35],[40],[41],[42],[43],[44],[60],[61],[65]])

se=[]
for i in range(1,15):
    model=KMeans(n_clusters=i,max_iter=100,n_init=1)
    """UserWarning: KMeans is known to have a memory leak on Windows with MKL,
    when there are less chunks than available threads.
    You can avoid it by setting the environment variable OMP_NUM_THREADS=1."""

    """The default value of `n_init` will change from 10 to 'auto' in 1.4.
    Set the value of `n_init` explicitly to suppress the warning"""

    model.fit(data)
    se.append(model.inertia_)#index to find best number of clusters
    print(model.labels_)
    print(model.cluster_centers_)
    print("_____________")

    
    
import matplotlib.pyplot as plt
plt.plot(range(1,15),se)
plt.ylabel("elbow")
plt.xlabel("cluster number")
plt.show()

si=[]
from sklearn.metrics import silhouette_score

for i in range(2,15):
    model=KMeans(n_clusters=i,n_init=1,max_iter=100)
    model.fit(data)
    si.append(silhouette_score(data,model.labels_))#index to find best number of clusters

plt.plot(range(2,15),si)
plt.ylabel("silhoutte")
plt.xlabel("cluster number")
plt.show()

