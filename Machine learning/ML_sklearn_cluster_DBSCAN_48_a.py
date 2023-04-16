from sklearn.cluster import DBSCAN
import numpy as np

X = np.array([[7, 3], [7, 4], [8, 3],[9, 3], [5, 2], [4, 3],[3,3]])
model = DBSCAN(eps=2, min_samples=2)
model.fit(X)
print(model.labels_)
print(model.fit_predict([[8,4]]))
