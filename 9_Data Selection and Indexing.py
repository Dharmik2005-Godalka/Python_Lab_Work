import pandas as pd

Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'],
        'Age': [28, 23, 35, 31],
        'Gender': ['M', 'F', 'M', 'F']
        }
df = pd.DataFrame(Biodata)

dat = pd.read_csv("data.csv")
print(dat[['Name']])
print(dat[['Name','Number']])
print(dat.loc[[1]])
