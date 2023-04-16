import pandas as pd
import matplotlib.pyplot as plt

data={"day1":[23,26,27],
      "day2":[24,25,26],
      "day3":[25,27,29],
      "day4":[25,26,28]}
y=pd.DataFrame(data,index=["TEH","SA","HA"])
print(y)
print("++++++++++++++++++")
print(y.loc[:"SA",["day1","day4"]])
print("========== statistics ============")
print("")
print(y.describe())
print("--------correlation-------------")
print(y.corr())#همبستگي


#plots in dataframe
#y2=pd.DataFrame(data)
#y2.plot(kind="line",x="day1",y="day2")
#y2.plot(kind="scatter",x="day3",y="day2")
#y2.plot(kind="bar",x="day1",y="day2")
#y2.plot(kind="pie",y="day1")
#plt.show()
y.plot.bar()#comparing bar plots near ech other
#y.plot.barh() Horizental
plt.show()

