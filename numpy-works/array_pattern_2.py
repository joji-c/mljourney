"""
4  4  4  4  4
4  1  1  1  4
4  1 100 1  4
4  1  1  1  4
4  4  4  4  4 
"""
import numpy as np

"""array=np.full((5,5),4)
array[1:4,1:4]=1
array[2,2]=100
print(array)"""

array=np.full((5,5),4)
one_array=np.ones((3,3),dtype="int")
one_array[1,1]=100
array[1:4,1:4]=one_array
print(array)
