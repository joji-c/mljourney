import numpy as np

price=np.array([100,120,450,75])

discount_price = price - 10
print(discount_price)

new_price = price + 10
print(new_price)

arr1=np.array([[1,2],
               [3,4]])
arr2=np.array([[10,11],
               [12,13]])
arr3=np.array([10,11])
print(arr1+arr2)
print(arr1+arr3)
