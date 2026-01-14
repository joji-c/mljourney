import pandas as pd
students={
    "name":["adhnan","adhil","rafi","jacob","jane"],
    "age":[23,22,24,25,27],
    "course":["ds","ds","ml","ai","ai"]
}
df = pd.DataFrame(students)
print(df)
print(df[1:2])
print(df[["name","course"]])
print(df[["name","age"]])