import numpy as np

arr1=np.array([
    [
        [10,11],
        [12,13]
    ],
    [
        [100,110],
        [120,130]
    ]
])
print(arr1.ndim)
print(arr1.shape)
print(arr1[1,0,0]) #find 100
print(arr1[0,1,1]) #find 13
print(arr1[1,1,1]) #find 130
print(arr1[0,0,1]) #find 11
arr1[1,1,0]=125
arr1[1,0,1]=11
print(arr1)
