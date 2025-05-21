import pandas as pd

'''Create a series'''
s1 = pd.Series([1, 3, 5, 7, 9])
# print(s1)

'''Create a series with custom index'''
s2 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
# print(s2)

'''Create a series from a dictionary'''
d = {'a': 1, 'b': 3, 'c': 5, 'd': 7, 'e': 9}
s3 = pd.Series(d)
# print(s3)

'''Access elements in a series'''
print(s3[0])
print(s3['a'])
print(s3[:3])
print(s3[['a', 'c', 'e']])

'''Create a DataFrame'''
data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Minnie'], 'Age': [10, 20, 30, 40]}
df = pd.DataFrame(data)
# print(df.columns)
# print(df)

'''Create a DataFrame with custom index'''
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
# print(df)

'''Create a DataFrame from a list of dictionaries'''
data = [{'Name': 'Tom', 'Age': 10}, {'Name': 'Jerry', 'Age': 20}, {'Name': 'Mickey', 'Age': 30}, {'Name': 'Minnie', 'Age': 40}]
df = pd.DataFrame(data)
# print(df)

'''Create a DataFrame from a dictionary of Series'''
data = {'Name': pd.Series(['Tom', 'Jerry', 'Mickey', 'Minnie']), 'Age': pd.Series([10, 20, 30, 40])}
df = pd.DataFrame(data)
# print(df)

'''Insertion and Delection in data'''
data = {'Num1': [2, 5, 8, 8, 5, 2], 'Age': [20, 50, 80, 80, 50, 20]}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E', 'F'])
# print(df)
# print('-------------------------')

df.insert(2,'test_',(df['Num1']+df['Age']))
df['test'] = df['Num1'] >= 8
# print(df)
print('-------------------------')
df.pop('test_')
# print(df)
# df.head()         # First 5 rows
# df.tail()         # Last 5 rows
# df.info()         # Column info: types, non-nulls
# df.describe()     # Stats for numeric columns
# df.columns        # List of column names
# df.shape          # (rows, columns)

'''Create a DataFrame from a dictionary of dictionaries'''
data = {'Name': {'A': 'Tom', 'B': 'Jerry', 'C': 'Mickey', 'D': 'Minnie'}, 'Age': {'A': 10, 'B': 20, 'C': 30, 'D': 40}}
df = pd.DataFrame(data)
# print(df)

'''-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-'''
# '''save the DataFrame to a CSV file'''
df.to_csv('Test_File.csv',index=False)

'''read the CSV file'''
df = pd.read_csv(r'\Test_data.csv')
# print(df)

# print(df.isnull()) # to check the null values location
# print(df.isnull().sum())  # to check the null values count
df.dropna()              # Drop rows with *any* missing values
df.dropna(axis=1)        # Drop columns with missing values

df.fillna(0)                     # Replace NaN with 0
df["Age"].fillna(df["Age"].mean())  # Replace with mean
df.ffill()      # Forward fill
df.bfill()      # Backward fill

''' Detecting & Removing Duplicates'''
df.duplicated(subset=["Name", "Age"])

''' String Operations with `.str`------------------------------'''
df["Name"].str.lower() # Converts all names to lowercase.
df["City"].str.contains("delhi", case=False) # Checks if 'delhi' is in the city name, case-insensitive.
df["Email"].str.split("@") # Outputs a pandas Series where each element is a list of strings (the split parts)

''' Type Conversions with `.astype()`---------------------------'''
df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])
df["Category"] = df["Category"].astype("category")

''' Applying Functions----------------------------------------'''
# `.apply()` → Apply any function to rows or columns
df["Age Group"] = df["Age"].apply(lambda x: "Adult" if x >= 18 else "Minor")

# `.map()` → Element-wise mapping for Series
gender_map = {"M": "Male", "F": "Female"}
df["Gender"] = df["Gender"].map(gender_map)

# `.replace()` → Replace specific values
df["City"].replace({"Del": "Delhi", "Mum": "Mumbai"})


''' Groupby'''
df = pd.DataFrame({
    "Department": ["HR", "HR", "IT", "IT", "Marketing", "Marketing", "Sales", "Sales"],
    "Team": ["A", "A", "B", "B", "C", "C", "D", "D"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Salary": [85, 90, 78, 85, 92, 88, 75, 80],
    "Age": [23, 25, 30, 22, 28, 26, 21, 27],
    "JoinDate": pd.to_datetime([
        "2020-01-10", "2020-02-15", "2021-03-20", "2021-04-10",
        "2020-05-30", "2020-06-25", "2021-07-15", "2021-08-01"
    ])
})

# print(df.groupby("Department")["Salary"].mean())
# df.groupby("Team")["Salary"].mean()     # Average per team
# df.groupby("Team")["Salary"].sum()      # Total score
# df.groupby("Team")["Salary"].count()    # How many entries
# df.groupby("Team")["Salary"].min()
# df.groupby("Team")["Salary"].max()

# df.groupby(["Team", "Gender"])["Salary"].mean() # To group by multiple columns

''' Custom Aggregations with `.agg()`'''
df.groupby("Team")["Salary"].agg(["mean", "max", "min"])

df.groupby("Team")["Salary"].agg(
    avg_score="mean",
    high_score="max"
)

df.groupby("Team").agg({        # Apply different functions to different columns
    "Salary": "mean",
    "Age": "max"
})

''' `.filter()` Function'''
df.groupby("Team").filter(lambda x: x["Salary"].mean() > 80)

'''Marging & joining'''
employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DeptID": [10, 20, 30]
})

departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "DeptName": ["HR", "Engineering", "Marketing"]
})
pd.merge(employees, departments, on="DeptID")               # Inner join
pd.merge(employees, departments, on="DeptID", how="left")   # Left join
pd.merge(employees, departments, on="DeptID", how="right")  # Right Join
pd.merge(employees, departments, on="DeptID", how="outer")  # Outer Join

