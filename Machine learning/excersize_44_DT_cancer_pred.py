import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import confusion_matrix,classification_report

data=pd.read_excel("excersize_42_cancer_pred.xlsx")
x=data.iloc[:,1:-1].values
y=data.iloc[:,-1].values

X_train,X_test,y_train,y_test= train_test_split(x,y,test_size=0.25,random_state=0)
model= DecisionTreeClassifier()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(y_pred)


#print(confusion_matrix(y_test,y_pred))
#print(classification_report(y_test,y_pred))

risc=model.predict([[0,45,1]])
print("cancer Risc:",risc)

plot_tree(model)
plt.show()
