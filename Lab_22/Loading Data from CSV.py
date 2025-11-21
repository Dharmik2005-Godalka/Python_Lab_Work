import pandas as pd

csv = 'sample_data.csv'
df = pd.read_csv(csv)

print("CSV Data:")
print(df)

a = df[df['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(a)
