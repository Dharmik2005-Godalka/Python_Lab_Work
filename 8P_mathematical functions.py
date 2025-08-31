import math

def evaluate_math(x):
    return math.exp(x), math.log2(x), math.sqrt(abs(x))

# Example usage
x = 4
expx, log2x, sqrtx = evaluate_math(x)
print("exp:", expx)
print("log2:", log2x)
print("sqrt(abs):", sqrtx)
