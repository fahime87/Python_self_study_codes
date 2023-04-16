import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
data=np.array([[60,2,4,10,1,620],
      [80,2,2,5,1,920],
      [40,1,1,15,1,360],
      [75,2,2,5,2,1125],
      [90,3,4,10,2,1170],
      [35,1,1,2,2,560],
      [50,1,3,10,2,700],
      [80,2,5,5,3,1600],
      [100,3,4,10,3,1800],
      [50,1,1,2,3,1000]])
x=data[:,:-1]
y=data[:,-1]
model = linear_model.LinearRegression()
model.fit(x, y)
x_test=x
y_test=y
y_pred= model.predict(x_test)

print(y)
print("r2=",r2_score(y_test,y_pred))
y_predict=model.predict([[70,1,2,17,2]])
print("price=",y_predict)


plt.scatter(range(1,11),y,label="data")
plt.plot(range(1,11),y_pred,label="predict")
plt.legend()
plt.show()
