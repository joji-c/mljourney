import numpy as np

attendance = [  
  #m  t  w  h  f
  [1, 1, 1, 1, 1], # Student 1
  [1, 0, 1, 1, 1], # Student 2
  [1, 1, 0, 1, 1], # Student 3
  [0, 1, 1, 1, 0], # Student 4
  [1, 1, 1, 0, 1], # Student 5
  [1, 0, 0, 1, 1], # Student 6
  [1, 1, 1, 1, 0], # Student 7
  [0, 1, 1, 0, 1], # Student 8
  [1, 1, 0, 1, 0], # Student 9
  [1, 0, 1, 1, 1]  # Student 10
]

#functions -> sum,max,min,avg,count_nonzero
arr = np.array(attendance)

#display column 5
print(arr[:,4])

#display row 10
print(arr[9])

#update student  value in row 7,column 5
arr[6,4]=1
print(arr[6])

#function sum
print(np.sum(arr,axis=1))          #axis=1 means rows
print(np.sum(arr,axis=0))          #axis=0 means columns

#function count_zero           #count_zero helps in counting any specific value in an array
stud_ab=np.count_nonzero(arr==0,axis=1)          
print(stud_ab)
day_ab=np.count_nonzero(arr==0,axis=0)
print(day_ab)

