import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")

# Dataset:
x = np.random.RandomState(10)
d = x.normal(size=100)

# Histogram:
sns.histplot(d, kde=True, color="m")
plt.show()
