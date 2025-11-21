import pandas as pd

excel = 'sample_data.xlsx'
df = pd.read_excel(excel)

print("\nExcel Data:")
print(df)

count = df.shape[0]
print("\nNumber of entries in Excel file:", count)
