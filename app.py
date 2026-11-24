import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("sales.csv")

print(df.info())
print(df.describe())
print(df.head())


df.isnull().sum()
df.duplicated().sum()

df['City'].value_counts()
df['City'].value_counts().plot(kind="bar")
plt.title("City Distribution")
plt.show()
