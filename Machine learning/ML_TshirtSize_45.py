"""
 predicting T_shirt size by cosidering weight and height
 comparing 3 machine learning algorim:
     1_logisticRegression
     2_decisionTree
     3_KNN algorim)
 testing precision of prediction model by indexes
 tuesday,April 11,2023
"""
__outhor__="Fahime Ameri"
__email__="fahime.ameri87@yahoo.com"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data=pd.read_excel("T_shirt.xlsx")#read data from xlsx file
x=data.iloc[: ,:-1]
y=data.iloc[:,-1]
print(data.shape)
print("___________________________")
print(data)
print("===========================")
print(data.describe())


#++++++++++++++++++++++++++machin learning part and 3 technique++++++++++++++++

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)#we use 20 % of data for testing our model precision
#logistic
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()#making model
model.fit(xtrain,ytrain)#train the model
ypred=model.predict(xtest)#predict the T_shirt size
print("_______________________")
print("Logistic=",ypred)

#decision tree
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()#making decision tree
model.fit(xtrain,ytrain)#train the model
ypred=model.predict(xtest)#predict the T_shirt size
print("_______________________")
print("Decision Tree=",ypred)

 
#decision tree
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=1)#making KNN model
model.fit(xtrain,ytrain)#train the model
ypred=model.predict(xtest)#predict the T_shirt size
print("_______________________")
print("KNN=",ypred)
