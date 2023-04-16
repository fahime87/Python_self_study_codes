import pandas as pd
import os
os.environ["OMP_NUM_THREADS"] = '1'
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
data=pd.read_csv("Wholesale customers data.csv")
print(data.shape)
mms=MinMaxScaler()
mms.fit(data)
x=mms.transform(data)
#x=data.iloc[:,:].values
EL=[]
sc=[]
for i in range(2,25):
    model=KMeans(n_clusters=i,n_init=1)
    model.fit(x)
    EL.append(model.inertia_)
    sc.append(silhouette_score(x,model.labels_))

plt.plot(range(2,25),EL,label="elbow")

plt.legend()
plt.show()
    
plt.plot(range(2,25),sc,label="silhouette")
plt.legend()
plt.show()
