import numpy as np
# np.loadtxt(file_path,delimeter,skip_rows,dtype)
data=np.loadtxt("numpy-works\\sales\\sales.csv",delimiter=",",skiprows=1,dtype="str")
print(data)
# total units sold
units_sold=data[:,3].astype("int")
total_units=np.sum(units_sold)
print(total_units)
# max unit
max_unit=np.max(units_sold)
print(max_unit)
# min unit
min_unit=np.min(units_sold)
print(min_unit)
# avg unit
avg_unit=np.average(units_sold)
print(avg_unit)
# revenue
price=data[:,4].astype("int")
revenue=units_sold*price
print(units_sold,revenue)
# total revenue
print(np.sum(revenue))
# units sold greater than 8
print(data[units_sold>8])
# category electronics
category=data[:,2]
print(data[category=="Electronics"])
# flat 100 discount
data[:,4]=data[:,4].astype("int")-100
print(data)
# total revenue of north region
north_data=data[data[:,-1]=="North"] 
print(north_data)
revenue_north=[north_data[:,3].astype("int")*north_data[:,4].astype("int")]
print(np.sum(revenue_north))
