import numpy as np
data = np.genfromtxt("titanic-case-study\\passenger_data.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
# loadtxt gives error for null values in csv
print(f"total number of passengers {data.shape}")
# total no. of survivals
survivors=np.count_nonzero(data[:,1].astype("int")==1)
print(survivors)
# total no. of non survivors
non_survivors=np.count_nonzero(data[:,1].astype("int")==0)
print(non_survivors)
# survival rate
total_passengers=np.count_nonzero(data[:,0].astype("int"))
survival_rate=(survivors/total_passengers)*100
print(survival_rate)
# non survived rate
non_survival_rate=(non_survivors/total_passengers)*100
print(non_survival_rate)
# gender analysis
male_passengers=data[data[:,3]=="male"]
total_male_count=np.count_nonzero(male_passengers[:,0].astype("int"))
print(total_male_count)
male_survivors=np.count_nonzero(male_passengers[:,1].astype("int")==1)
print(male_survivors)
female_passengers=data[data[:,3]=="female"]
total_female_count=np.count_nonzero(female_passengers[:,0].astype("int"))
print(total_female_count)
female_survivors=np.count_nonzero(female_passengers[:,1].astype("int")==1)
print(female_survivors)
male_survival_rate=(male_survivors/total_male_count)*100
print(male_survival_rate)
female_survival_rate=(female_survivors/total_female_count)*100
print(female_survival_rate)
"""survived_males=data[(data[:,3]=="male")&(data[:,1].astype("int")==1)]
survived_male_count=survived_males[:,0].size
male_survival_rate=(survived_male_count/total_male_count)*100"""
# age analysis
max_age=np.max(data[:,4].astype("int"))
print(data[data[:,4].astype("int")==max_age])
min_age=np.min(data[:,4].astype("int"))
print(data[data[:,4].astype("int")==min_age])
avg_age=np.average(data[:,4].astype("int"))
print(avg_age)
# fare analysis
max_fare=np.max(data[:,5].astype("float"))
print(max_fare)
min_fare=np.min(data[:,5].astype("float"))
print(min_fare)
average_fare=np.average(data[:,5].astype("float"))
print(average_fare)
# sorting
print(data[np.argsort(data[:,-2].astype("float"))])