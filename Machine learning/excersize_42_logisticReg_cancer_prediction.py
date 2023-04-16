import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_excel("excersize_42_cancer_pred.xlsx")

x=data.iloc[:,1:-1].values
y=data.iloc[:,-1].values
model=LogisticRegression()
model.fit(x,y)
y_pred=model.predict([[0,45,1]])
print("cancer Risk",y_pred)
