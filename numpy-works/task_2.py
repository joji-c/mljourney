import numpy as np

productivity = np.array([
    #1  2  3  4  5  6  7  8  9  10
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],  #emp1
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],  #emp2
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],  #emp3
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],  #emp4
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],  #emp5
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]   #emp6
])

emp_hour=np.sum(productivity,axis=1)
print(emp_hour)
day_hour=np.sum(productivity,axis=0)
print(day_hour)
emp_avg_hour=np.average(productivity,axis=1)
print(emp_avg_hour)
day_avg_hour=np.average(productivity,axis=0)
print(day_avg_hour)
max_emp_hour=np.argmax(emp_hour)
print(max_emp_hour)
min_emp_hour=np.argmin(emp_hour)
print(min_emp_hour)
max_day_hour=np.argmax(day_hour)
print(max_emp_hour)
overworked=emp_avg_hour>8
print(emp_avg_hour[overworked])
most_least_diff=np.max(emp_hour)-np.min(emp_hour)
print(most_least_diff)