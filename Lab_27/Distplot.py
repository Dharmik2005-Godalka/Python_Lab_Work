import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# Dataset:
data = np.random.randn(200)

# Distplot:
sns.distplot(data, kde=True, hist=True, rug=False)
plt.show()
