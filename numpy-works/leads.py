import numpy as np

leads = np.array([
    #s   m   t   w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
])

#total lead generated each day
each_day=np.sum(leads,axis=0)
print(each_day)

#total lead generated in seven days
source_leads=np.sum(leads,axis=1)
print(source_leads)

#highest lead day index
max_lead=np.max(leads,axis=0)
print(max_lead)
print(np.max(each_day))                                #max gives the max value
print("column of max day leads:",np.argmax(each_day))       #argmax gives the index of the max value

#avg leads per source
avg_lead_source=np.average(leads,axis=1)
print(avg_lead_source)

#avg leads per day
avg_lead_day=np.average(leads,axis=0)
print(avg_lead_day)

#highest lead source
print(np.max(source_leads))
print("row of max source leads:",np.argmax(source_leads))
