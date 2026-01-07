"""
1 2 3
4 5 6
7 8 9
"""

import numpy as np

two_dimensional_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(two_dimensional_array)
print(two_dimensional_array.ndim)
print(two_dimensional_array.size)         #get num of value in array
print(two_dimensional_array.shape)        #get the shape of the array
