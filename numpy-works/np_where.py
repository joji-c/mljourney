# np.where(condition,true_value,false_value)
import numpy as np
ages=np.array([19,20,17,16,20,21])
print(np.where(ages>=20,"Adults","Teen"))
