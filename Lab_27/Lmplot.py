import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")

data = sns.load_dataset("anscombe")

sns.lmplot(x="x", y="y", data=data)
plt.show()
