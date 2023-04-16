from sklearn.cluster import DBSCAN
import numpy as np
from matplotlib import pyplot as plt
from sklearn.neighbors import NearestNeighbors
X = np.array([[1, 2], [2, 2], [2, 3],
[8, 7], [8, 8], [25, 80]])

neighbors = NearestNeighbors(n_neighbors=2)
neighbors_fit= neighbors.fit(X)
distances, indices = neighbors_fit.kneighbors(X)

distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)
plt.show()
model = DBSCAN(eps=1.1, min_samples=2)
model.fit(X)
print(model.labels_)
