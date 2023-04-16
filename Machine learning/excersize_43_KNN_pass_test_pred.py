import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report

data=pd.read_excel("excersize_42_test_score_pred.xlsx")
x=data.iloc[:,1:-1].values
y=data.iloc[:,-1].values
X_train,X_test,y_train,y_test= train_test_split(x,y,test_size=0.30)
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)



print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

test_res=model.predict([[40,2]])
print("pass test:",test_res)
