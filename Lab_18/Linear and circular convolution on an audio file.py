import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

fs1, x = wavfile.read(r"C:\Users\Dharmik\COLLEGE\SEM-3\Python\Lab's Code\Lab_18\Audio_1 (1).wav")
fs2, h = wavfile.read(r"C:\Users\Dharmik\COLLEGE\SEM-3\Python\Lab's Code\Lab_18\Audio_2 (1).wav")

if x.ndim > 1: 
    x = x[:, 0]
if h.ndim > 1: 
    h = h[:, 0]

# float:
x = x[:2000].astype(float)
h = h[:500].astype(float)

# Linear convolution
n = len(x)
m = len(h)
linear = np.zeros(n + m - 1)
for i in range(n):
    linear[i:i+m] += x[i] * h

# Circular convolution
N = max(n, m)
X = np.pad(x, (0, N - n))
H = np.pad(h, (0, N - m))
circular = np.zeros(N)
for i in range(N):
    circular[i] = np.sum(X * np.roll(H, i))

x = x / np.max(np.abs(x))
linear = linear / np.max(np.abs(linear))
circular = circular / np.max(np.abs(circular))

# Plot:
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(x, color='blue')
plt.title("My Audio Signal")

plt.subplot(3, 1, 2)
plt.plot(linear, color='green')
plt.title("Linear Convolution")

plt.subplot(3, 1, 3)
plt.plot(circular, color='red')
plt.title("Circular Convolution")

plt.tight_layout()
plt.show()

