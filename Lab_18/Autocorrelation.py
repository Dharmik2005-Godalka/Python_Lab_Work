import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

p = len(x) - 1
a = [0]*p + x + [0]*p

auto = []
for i in range(len(x) + len(x) - 1):
    s = 0
    for j in range(len(x)):
        s += a[i + j] * x[j]
    auto.append(s)

print("Autocorrelation:", auto)

# Plot:
plt.stem(auto)
plt.title('Autocorrelation')
plt.xlabel('Lag')
plt.ylabel('Amplitude')
plt.show()
