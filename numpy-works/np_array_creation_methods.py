import numpy as np
#np.array(list)
#np.zeros((shape))
#np.ones((shape))
#np.full((shape),value)
#np.random.rand(shape)
#np.random.randint(low,high,(shape))

zero_array=np.zeros((2,3),dtype="int")
print(zero_array)

one_array=np.ones((3,2),dtype="int")
print(one_array)

full_array=np.full((3,3),5)
print(full_array)

random_array=np.random.rand(2,4)
print(random_array)

random_int_array=np.random.randint(1,10,(4,4))
print(random_int_array)
