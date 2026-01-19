import pandas as pd
df = pd.read_csv("pandas-works\\task3\\malayalam_actors_actresses.csv")

print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())

#oldest actor
print(df.loc[df["age"].idxmax(),"name"])
#youngest actor
print(df.loc[df["age"].idxmin(),"name"])

#avg num of films per actor
print(df.groupby("name")["no_of_films"].mean())

#current active status
print(df["active_status"].value_counts())

#debut after 2000
print(df[df["debut_year"]>2000])