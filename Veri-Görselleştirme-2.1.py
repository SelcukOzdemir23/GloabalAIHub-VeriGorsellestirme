import seaborn as snb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = snb.load_dataset("planets") # Pandas
df = data.copy()
result = df.head(10)
result = df.info()
result = df.dtypes

df["method"] = pd.Categorical(df.method) #Kategorik yaptık
result = df.dtypes
#for information
result = df.head()

result = df.shape
result = df.columns
result = df.describe().T

result = df.describe(include="all") #Artık string değerler de işleniyor
result = df.nunique()
result = df.isna().values.any()
result = df.isna().sum()

#fill nan-parts
df["mass"].fillna(df.mass.mean(),inplace=True)
result = df.isna().sum()
result = df.mean()
df.fillna(df.mean(),inplace=True)
result = df.isna().sum()

result = df.head()
result = kat_df = df.select_dtypes(include=["category"])
result = kat_df.head()
result = kat_df.method.unique()
result = kat_df.method.nunique()
result = len(kat_df.method.unique())
result = kat_df.method.value_counts().sort_values().plot.barh()

plt.show()




