import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split

data=pd.read_excel("excersize_42_test_score_pred.xlsx")
x=data.iloc[:,1:-1].values
y=data.iloc[:,-1].values
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)

model=LogisticRegression()
model.fit(xtrain,ytrain)
y_pred=model.predict(xtest)

print(confusion_matrix(ytest,y_pred))
print(classification_report(ytest,y_pred))

test_res=model.predict([[40,2]])
print("pass the exam",test_res)
