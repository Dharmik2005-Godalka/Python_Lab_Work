x = [1, 2, 3, 4]
h = [1, 0, -1]

n = len(x)
m = len(h)
y = [0] * (n + m - 1)

for i in range(n):      
    for j in range(m):    
        y[i + j] += x[i] * h[j]  

print("Linear Convolution:", y)
