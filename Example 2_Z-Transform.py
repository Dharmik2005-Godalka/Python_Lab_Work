import sympy as sp

# Define symbols
n, z = sp.symbols('n z')

# Define the signal x[n] = 2^n * u[n]
x_n = 2**n

# Compute the Z-transform
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

# Print the result
print("Z-transform of x[n] = 2^n u[n]:")
sp.pprint(X_z, use_unicode=True)
