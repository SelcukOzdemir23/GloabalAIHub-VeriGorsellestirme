from cProfile import label
from re import T
import matplotlib.pyplot as plt
import numpy as np


result = x = np.arange(0,9)
result = y = x**2

# plt.plot(x,y)
# plt.xlabel("Kareler")
# plt.ylabel("Sayılar")
# plt.show()

#SCATTER PLOT

x = 20*np.random.randn(500)+100
y = x+(10*np.random.randn(500))+50
# plt.scatter(x,y,color="r")
# plt.show()

#BAR PLOT

x = ["COVİD-19","HEALTHY","SYMPTOMATIC"]
y = [1010,8562,1843]
color=["r","g","b"]
# plt.bar(x,y,color=color,width=0.1)
# plt.plot(x,y,color="purple")
# plt.show()

#HISTOGRAM PLOT

import seaborn as sns
penguins = sns.load_dataset("penguins") #Pandas
result = penguins.head()
# sns.displot(data=penguins,x = "island")
# plt.show(block=True)
result = penguins.columns

#PIE CHART

etiketler = ["Osman","Ali","Sevim","Salih","Hüsniye"]
maaslar = [1000,1100,500,10000,16000]
color = ["r","g","purple","b","black"]
# plt.pie(maaslar,labels=etiketler,colors=color)
# plt.show()

#HEAT MAPS

data = np.random.randn(10,12)
# sns.heatmap(data)
# plt.show(block=True)


#BOX PLOT
tips = sns.load_dataset("tips")
tips = tips[tips["total_bill"]<35]
result = tips.head()
# sns.boxplot(x=tips["total_bill"])
# plt.show() 


#SON

result = x = np.arange(1,9)
y= x**2
x2 = np.arange(1,9)
y2 = x2**3

# plt.plot(x,y,label="X^2 Değerleri")
# plt.plot(x2,y2,color="purple",label="X^3 Değerleri")

# plt.xlabel("Sayilar")
# plt.title("X^2 Grafiği")
# plt.ylabel("Kareler")

# plt.grid()
# plt.legend()
# plt.show()

#SUBPLOT

fig = plt.figure(figsize=(5,15))

firstPlot = fig.add_subplot(3,1,1)
secondPlot = fig.add_subplot(3,1,2)
thirdPlot = fig.add_subplot(3,1,3)

firstPlot.plot(x,y,color="purple")
firstPlot.set_title("Kare")
firstPlot.grid()

secondPlot.scatter(x2,y2,color="red")
secondPlot.set_title("Küp")
secondPlot.grid()

thirdPlot.bar(x,y,color="blue")
thirdPlot.set_title("Bar")
thirdPlot.grid()

print(result)
plt.show()