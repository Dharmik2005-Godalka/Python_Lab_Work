import pandas as pd

df = pd.read_csv("sample_data.csv")

df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nMissing values:\n")
print(df)
