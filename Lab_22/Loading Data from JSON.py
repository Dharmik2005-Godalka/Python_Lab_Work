import pandas as pd

json = 'sample_data.json'
df = pd.read_json(json)

print("\nJSON DATA:")
print(df)

average = df['Age'].mean()
print("\nAverage Age:", average)
