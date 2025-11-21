import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="dark")

f = sns.load_dataset("fmri")

# Lineplot:
sns.lineplot(
    x="timepoint",
    y="signal",
    hue="region",
    style="event",
    data=f)

plt.show()
