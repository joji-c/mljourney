# task1 even or odd
import numpy as np
array=np.array([2,3,4,5,6,7,8])
print(np.where(array%2==0,"even","odd"))

# task2 pos or neg
array=np.array([-1,2,3,-2,5])
print(np.where(array>=0,"+ve","-ve"))
