import pandas as pd
import os
os.environ["OMP_NUM_THREADS"] = '1'
data_r=pd.read_excel("excersize_country_crim_data.xlsx")
print (data_r)
data=data_r.iloc[:,1:].values
from sklearn.preprocessing import MinMaxScaler

mms=MinMaxScaler()
mms.fit(data)
data1=mms.transform(data)
from sklearn.cluster import KMeans

model=KMeans(n_clusters=3,n_init=1)
model.fit(data1)
print(model.labels_)


