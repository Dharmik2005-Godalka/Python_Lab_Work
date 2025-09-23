import sympy as sp

# Define symbols
n, z = sp.symbols('n z')

# Define the unit step signal u[n] = 1 for n ≥ 0
u_n = 1

# Compute the Z-transform
U_z = sp.summation(u_n * z**(-n), (n, 0, sp.oo))

# Print the result
print("Z-transform of the unit step signal u[n]:")
sp.pprint(U_z, use_unicode=True)
