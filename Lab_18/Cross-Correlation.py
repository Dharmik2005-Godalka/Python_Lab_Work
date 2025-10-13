import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

p = len(y) - 1
a = [0]*p + x + [0]*p

c = []
for i in range(len(x) + len(y) - 1):
    s = 0
    for j in range(len(y)):
        s += a[i + j] * y[j]   
    c.append(s)

print("Cross-Correlation:", c)

# Plot:
plt.stem(c)
plt.title('Cross-Correlation')
plt.xlabel('Lag')
plt.ylabel('Amplitude')
plt.show()
