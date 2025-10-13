x = [1, 2, 3, 4]
h = [1, 0, -1]

N = len(x)
y = [0] * N

for n in range(N):
    for k in range(len(h)):
        y[n] += x[(n - k) % N] * h[k]

print(y)
