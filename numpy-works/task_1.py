import numpy as np

array=np.array([
    [43,42,45,34,23],
    [23,45,45,34,37],
    [37,38,39,40,45]
])

print(array[1])
print(array[1,0])
print(array[:,2])
print(array[:,2:4])
print(array[1:3,1:3])