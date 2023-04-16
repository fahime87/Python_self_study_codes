import os
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from matplotlib import pyplot as plt

os.environ["OMP_NUM_THREADS"] = '1'
data_r=pd.read_excel("excersize_country_crim_data.xlsx")
print (data_r)
X=data_r.iloc[:,1:].values

neighbors = NearestNeighbors(n_neighbors=2)
neighbors_fit= neighbors.fit(X)
distances, indices = neighbors_fit.kneighbors(X)

distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)
plt.show()
model = DBSCAN(eps=1.5, min_samples=2)
model.fit(X)
print(model.labels_)
