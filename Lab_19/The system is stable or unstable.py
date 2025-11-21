import numpy as np

# Unit step:
n = [2]
d = [1, -0.4]

# Poles:
poles = np.roots(d)
print("Poles =", poles)

if abs(poles[0]) < 1:
    print("System is Stable")
else:
    print("System is Unstable")
