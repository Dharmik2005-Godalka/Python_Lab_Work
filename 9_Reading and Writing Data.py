import pandas as pd

dat = pd.read_csv("data.csv")
print(dat)

Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'],
        'Age': [28, 23, 35, 31],
        'Gender': ['M', 'F', 'M', 'F']
        }
df = pd.DataFrame(Biodata)

# Save the dataframe to a CSV file
df.to_csv('Biodata.csv', index=False)
