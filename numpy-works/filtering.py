import numpy as np

productivity = np.array([
#emp 1  2  3  4  5  6  7  8  9  10
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],  #mon
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],  #tue
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],  #wed
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],  #thu
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],  #fri
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]   #sat
])
#all productivity < 6
print(productivity[productivity<6])

#productivity btw 5 and 7
print(productivity[(productivity>=5) & (productivity<=7)])

#first employee working hour < 9
arr1=productivity[:,0]
print(arr1[arr1<9])

#last 2 emp hour < 7
arr2=productivity[:,8:]
print(arr2[arr2<7])

#change all value < 8 as zero
productivity[productivity<8]=0
print(productivity)
