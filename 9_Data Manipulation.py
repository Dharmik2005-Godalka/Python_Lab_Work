import pandas as pd

# Creating a DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
}

dat = pd.DataFrame(data)
print("Original DataFrame:\n", dat)

# Multiplying column 'A' by 2
dat['A'] = dat['A'] * 2
print("\nAfter multiplying A by 2:\n", dat)

# Adding a new column 'F' which is A + B
dat['F'] = dat['A'] + dat['B']
print("\nAfter adding column F (A+B):\n", dat)

# Dropping column 'A'
dat = dat.drop(columns=['A'])
print("\nAfter dropping column A:\n", dat)

# Dropping row with index 0
dat = dat.drop(index=[0])
print("\nAfter dropping row with index 0:\n", dat)
