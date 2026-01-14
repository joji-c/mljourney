import pandas as pd
student_total={"s1":450,"s2":475,"s3":500,"s4":600}
series=pd.Series(student_total)
print(series)
print(series["s3"])
print(series[0:2])
print(series["s1":"s2"])
# aggregate functions
# sum(),max(),min(),mean()
print("total",series.sum())
print("max",series.max())
print("min",series.min())
print("mean",series.mean())