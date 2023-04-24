"""
 --> evaluating the precision of KNN algoritm in two cases:
         1_ using raw data directly without any preprocessing
         2_ normalizing data and dimension reduction  by LDA algoritm
 --> evaluation index is : sklearn.metrics.accuracy_score
 --> using "Wine" dataset
 
 Monday,April 24,2023
"""
__outhor__="Fahime Ameri"
__email__="fahime.ameri87@yahoo.com"


from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

wine_data=load_wine()
#print(wine_data.DESCR)
print(wine_data.keys())
X=wine_data.data
Y=wine_data.target
xtrain,xtest,ytrain,ytest=train_test_split(X,Y)


first_model=KNeighborsClassifier(n_neighbors=4)
first_model.fit(xtrain,ytrain)
ypredict=first_model.predict(xtest)
print("raw data accuracy score:",accuracy_score(ytest, ypredict))

#######now we want to do some preprocessing on data, then evaluate KNN precision

#frist normalize data
from sklearn.preprocessing import StandardScaler
X=StandardScaler().fit_transform(X)
#now reduce the dimention of normalized data by LDA algoritm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
x_lda=LDA().fit(X,Y).transform(X)
#print (x_lda)
#plot the new data after reduce dimension
import matplotlib.pyplot as plt
plt.scatter(x_lda[Y==0,0],x_lda[Y==0,1],c="orange",label="y=0")
plt.scatter(x_lda[Y==1,0],x_lda[Y==1,1],c="yellow",label="y=1")
plt.scatter(x_lda[Y==2,0],x_lda[Y==2,1],c="blue",label="y=2")
plt.legend()
plt.show()
#after preprocessing on raw data define a KNN model to predict

x_train,x_test,y_train,y_test=train_test_split(x_lda,Y)
second_model=KNeighborsClassifier(n_neighbors=4)
second_model.fit(x_train,y_train)
y_predict=second_model.predict(x_test)
print("accuracy score by standardscaler normalize and LDA :",accuracy_score(y_test, y_predict))




