import pandas as pd
sales_report = [
    {"date": "2026-01-01", "product": "Laptop", "category": "Electronics", "quantity": 2, "price": 55000, "salesperson": "Anil"},
    {"date": "2026-01-01", "product": "Mouse", "category": "Electronics", "quantity": 5, "price": 500, "salesperson": "Meera"},
    {"date": "2026-01-02", "product": "Chair", "category": "Furniture", "quantity": None, "price": 3500, "salesperson": "Rahul"},
    {"date": "2026-01-02", "product": "Desk", "category": "Furniture", "quantity": 1, "price": None, "salesperson": "Rahul"},
    {"date": "2026-01-03", "product": "Pen", "category": "Stationery", "quantity": 20, "price": 10, "salesperson": None},
    {"date": "2026-01-03", "product": "Notebook", "category": "Stationery", "quantity": 10, "price": 50, "salesperson": "Anil"},
    {"date": None, "product": "Printer", "category": "Electronics", "quantity": 1, "price": 12000, "salesperson": "Meera"},
    {"date": "2026-01-04", "product": "Monitor", "category": "Electronics", "quantity": 2, "price": None, "salesperson": "Anil"},
    {"date": "2026-01-05", "product": None, "category": "Furniture", "quantity": 1, "price": 8000, "salesperson": "Rahul"},
    {"date": "2026-01-05", "product": "Table Lamp", "category": None, "quantity": 3, "price": 1500, "salesperson": "Meera"}
]

dt=pd.DataFrame(sales_report)
print(dt.shape)
print(dt.columns)
print(dt.info())
print(dt.head())
print(dt.tail())
print(dt.isnull().sum())

#how to add values to null spaces
dt["date"].fillna(dt["date"].mode()[0],inplace=True)
dt["product"].fillna("unknown",inplace=True)
dt["category"].fillna(dt["category"].mode()[0],inplace=True)
dt["quantity"].fillna(dt["quantity"].mean(),inplace=True)
dt["price"].fillna(dt["price"].mean(),inplace=True)
dt["salesperson"].fillna(dt["salesperson"].mode()[0],inplace=True)
print(dt)
print(dt.isnull().sum())

#filtering
print(dt[(dt["category"]=="Electronics") & (dt["quantity"]>2)])

#remove null value rows
dt.dropna(subset=["category"],inplace=True)

#get the number of each column value
print(dt["category"].value_counts())
print(dt["salesperson"].value_counts())

#group by columns
print(dt.groupby("category")["price"].sum())
print(dt.groupby("category")["quantity"].sum())

#sort by columns
print(dt.sort_values(by="price",ascending=False))

#select a row
print(dt.loc[2])
print(dt.iloc[2])

#max price
print(dt[dt["price"]==dt["price"].max()])
print(dt.loc[dt["price"].idxmax()])

#min price
print(dt[dt["price"]==dt["price"].min()])
print(dt.loc[dt["price"].idxmin()])

#adding new column
dt["revenue"] = dt["price"] * dt["quantity"]
print(dt)

#select row and column
print(dt.loc[0,["product","price"]])

