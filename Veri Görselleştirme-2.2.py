from turtle import width
from unicodedata import category
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snb

mucevherler = snb.load_dataset("diamonds")
data = mucevherler.copy()
result = data.head()

result = data.info()
result = data.describe().T
result = data["cut"].value_counts()
result = data["color"].value_counts()

from pandas.api.types import CategoricalDtype
result = data.cut.head()
result = data.cut  = data.cut.astype(CategoricalDtype(ordered=True))
result = data.cut.head()


#GÖRSELLEŞTİRME

# data.cut.value_counts().sort_values().plot.barh().set_title("Cut Sutünü")
# snb.barplot(x=data["cut"],y=data.cut.index)

# snb.catplot(x="cut",y="price",data=data)

# snb.barplot(x="cut",y="price",hue="color",data=data) # hue başka bir boyut katmıyor sadece o bakımdaan da gösteriyor

result = data.groupby(["cut","color"])["price"].mean() #arka planda dönen kod

# snb.distplot(data.price,hist=False) #Histogram çiziyor-plt.hist()
(snb.FacetGrid(data,hue="cut",height=5,xlim=(0,10000))).map(snb.kdeplot,"price",shade=True).add_legend()
plt.show(block=True)
print(result)
