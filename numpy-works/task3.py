import numpy as np
#1d
arr1=np.array([3,6,9,12,15,18])
print(arr1[2])

arr2 = np.array([5, 10, 15, 20, 25, 30])
print(arr2[2:5])

arr3 = np.array([2, 4, 6, 8, 10, 12])
print(arr3[arr3%2==0])

arr4 = np.array([11, 22, 33, 44, 55])
print(arr4[arr4>30])

arr5 = np.array([7, 14, 21, 28, 35])
arr5[arr5>20]=-1
print(arr5)

arr6 = np.array([1, 2, 3, 4, 5])
print(arr6[::2])

arr7 = np.array([10, 20, 30, 40])
print(arr7*2)

arr8 = np.array([100, 200, 300, 400, 500])
print(arr8[::-1])

#2d
arr9 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr9[0])
print(arr9[:,-1])

arr10 = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
print(arr10[arr10>10])
x=0,1,2
print(arr10[x,x])

arr11 = np.array([[1, 2], [3, 4], [5, 6]])
print(arr11*5)

arr12 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr12[:2,2:])

arr13 = np.array([[2, 4], [6, 8], [10, 12]])
arr14=arr13[:,0]*10 
print(arr14)
