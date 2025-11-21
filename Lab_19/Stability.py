import numpy as np

n = [0.5, -0.8, 0.315]
d = [1, -1.0, 0.24]  

poles = np.roots(d)

print("Poles of the system = ", poles)

stable = all(abs(p) < 1 for p in poles)

if stable:
    print("Result: The system is STABLE")
else:
    print("Result: The system is UNSTABLE")
