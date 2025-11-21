import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['Mohe', 'Karnal', 'Yrik', 'Jack'],
    'Age': [30, 21, 29, 28]
}

df = pd.DataFrame(data)

sns.violinplot(df["Age"])
plt.show()
