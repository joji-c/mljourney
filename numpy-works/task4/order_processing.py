import numpy as np
data=np.loadtxt("numpy-works\\online\\online_orders.csv",delimiter=",",skiprows=1,dtype="str")
print(data.shape)

quantity=data[:,3].astype("int")
print(np.sum(quantity))

unit_price=data[:,4].astype("int")
print(np.average(unit_price))

revenue=[quantity*unit_price]
print(data[:,0],revenue)

delivery_date=data[:,-2].astype("int")
print(np.where(delivery_date<5))

returned=data[:,-1]
print(np.count_nonzero(returned=="Yes"))
print(np.count_nonzero(returned=="No"))

discount=data[:,-3].astype("int")
print(np.average(discount))

new_array=np.where(delivery_date<=3,"fast","normal")
print(new_array)
