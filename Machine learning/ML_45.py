"""
 predicting student scores by cosidering hours of studing
 using machine learning algorim (linearRegression)
 testing precision of prediction model by indexes
 tuesday,April 11,2023
"""
__outhor__="Fahime Ameri"
__email__="fahime.ameri87@yahoo.com"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error

data=pd.read_csv("student_scores.csv")#read data from csv file
x=data.iloc[: ,:-1]
y=data.iloc[:,-1]
print(data.shape)
print("___________________________")
print(data)
print("===========================")
print(data.describe())
"""there is also a plot function in pandas mudule !!!!"""
#data.plot(x="Hours",y="Scores",style="o")
#plt.xlabel("H")
#plt.ylabel("S")
#plt.show()#by ploting data we have view of them so we can use linear model

#++++++++++++++++++++++++++machin learning part++++++++++++++++++++++++++++++

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)#we use 20 % of data for testing our model precision
model=LinearRegression()#making model
model.fit(xtrain,ytrain)#train the model
#model=ax+b
a=model.coef_
b=model.intercept_
print("_______________________")
print("model=",a,"X +",b)
ypred=model.predict(xtest)#predict some score to test the model
"""estimate error rate for model """
mean_y=np.mean(y)
MAE=mean_absolute_error(ytest,ypred)
MSE=mean_squared_error(ytest,ypred)
Rmse=np.sqrt(MSE)
"""is Rmse < 0.1*mean then prediction mode is acceptable"""
print("mean =",mean_y)
print("Rmse =",Rmse)

 

