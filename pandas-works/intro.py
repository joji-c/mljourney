import pandas as pd
data=[165,166,178,176,179]
series=pd.Series(data)
print(series)
# weight series
weight=[80,85,70,90,91,100,88,70,99,85]
weight_series=pd.Series(weight)
print(weight_series)

# head() lists top 5 records
# tails() lists last 5 records
print(weight_series.head())
print(weight_series.tail())
print(series.shape)

salary=[30000,34000,35000,36000]
series=pd.Series(salary)
print(series[0])
print(series[1])
print(series[1:3])
series=pd.Series(salary,index=["e1","e2","e3","e4"])
print(series["e3"])
print(series["e1":"e4"])
