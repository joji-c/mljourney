"""
7 7 7 7 7 7 7
7 7 0 0 0 7 7
7 7 0 1 0 7 7 
7 7 0 0 0 7 7
7 7 7 7 7 7 7
"""
import numpy as np

array=np.full((5,7),7)
array[1:4,2:5]=0
array[2,3]=1
print(array)

