import numpy as np

one_dimensional_array=np.array([1,2,3,4])
print(one_dimensional_array)
print(type(one_dimensional_array))          # <class 'numpy.ndarray'>      here 'nd' -> n dimensional
print(one_dimensional_array.ndim)           # used to find the number of dimensions

mult_two=one_dimensional_array*2            # in list we would have done an iteration and slowed down this process
print(mult_two)

