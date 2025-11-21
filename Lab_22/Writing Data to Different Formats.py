import pandas as pd

csv = pd.read_csv('sample_data.csv')
filter = csv[csv['Age'] > 30]

json = pd.read_json('sample_data.json')

excel = pd.read_excel('sample_data.xlsx')

#CSV:
filter.to_csv('filter_data.csv', index=False)
print("\nFilter data saved to 'filter_data.csv'.")

#JSON:
json.to_json('new_data.json', orient='records', lines=True)
print("JSON data saved to 'new_data.json'.")

#Excel:
excel.to_excel('new_data.xlsx', index=False)
print("Excel data saved to 'new_data.xlsx'.")
