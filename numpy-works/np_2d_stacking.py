import numpy as np

arr1=np.array([
    [1,2],
    [3,4]])
arr2=np.array([
    [10,20],
    [30,40]])

#vertical stacking
vert=np.vstack((arr1,arr2))
print(vert)

#horizontal stacking
hori=np.hstack((arr1,arr2))
print(hori)
