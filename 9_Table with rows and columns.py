import pandas as pd

# Creating a DataFrame from the dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Return row 0:
print(df.loc[[0]])

#Return row 0 and 1:
#use a list of indexes:
print(df.loc[[0, 1]])
