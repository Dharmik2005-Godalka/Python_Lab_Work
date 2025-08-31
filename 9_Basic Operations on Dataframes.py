import pandas as pd

# Creating a DataFrame from the dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)  

# Accessing Columns (select one column)
print(df[['Name']])

# Adding a New Column
df['Salary'] = [70000, 80000, 90000]
print(df)

# Dropping a Column
df = df.drop('City', axis=1)
print(df)
