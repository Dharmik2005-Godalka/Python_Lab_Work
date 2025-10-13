import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs1, clean = wavfile.read(r"C:\Users\Dharmik\COLLEGE\SEM-3\Python\Lab's Code\Lab_18\audio_3 (2).wav")
fs2, noisy = wavfile.read(r"C:\Users\Dharmik\COLLEGE\SEM-3\Python\Lab's Code\Lab_18\audio_4.wav")
fs3, periodic = wavfile.read(r"C:\Users\Dharmik\COLLEGE\SEM-3\Python\Lab's Code\Lab_18\audio_5.wav")

if clean.ndim > 1: 
    clean = clean[:, 0]
if noisy.ndim > 1: 
    noisy = noisy[:, 0]
if periodic.ndim > 1: 
    periodic = periodic[:, 0]

clean = clean[:4000].astype(float)
noisy = noisy[:4000].astype(float)
periodic = periodic[:4000].astype(float)

#formula:
def autocorrelation(x):
    n = len(x)
    r = np.zeros(2*n - 1)
    for l in range(-n + 1, n):
        for i in range(n):
            j = i + l
            if 0 <= j < n:
                r[l + n - 1] += x[i] * x[j]
    return r

def cross_correlation(x, y):
    n = len(x)
    m = len(y)
    r = np.zeros(n + m - 1)
    for lag in range(-m + 1, n):
        for i in range(n):
            j = i + lag
            if 0 <= j < m:
                r[lag + m - 1] += x[i] * y[j]
    return r

# Autocorrelation
acClean = autocorrelation(clean)
acNoisy = autocorrelation(noisy)
acPeriodic = autocorrelation(periodic)

# Cross-correlation
ccCleanNoisy = cross_correlation(clean, noisy)
ccCleanPeriodic = cross_correlation(clean, periodic)

# Normalization function
def normalize(x):
    x = x - np.mean(x)
    return x / np.max(np.abs(x))

# Normal signals:
acClean = normalize(acClean)
acNoisy = normalize(acNoisy)
acPeriodic = normalize(acPeriodic)
ccCleanNoisy = normalize(ccCleanNoisy)
ccCleanPeriodic = normalize(ccCleanPeriodic)

# Plot:
plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.plot(acClean, color='blue')
plt.title("Autocorrelation - Clean Audio")

plt.subplot(3, 2, 2)
plt.plot(acNoisy, color='green')
plt.title("Autocorrelation - Noisy Audio")

plt.subplot(3, 2, 3)
plt.plot(acPeriodic, color='orange')
plt.title("Autocorrelation - Periodic Audio")

plt.subplot(3, 2, 4)
plt.plot(ccCleanNoisy, color='red')
plt.title("Cross-Correlation - Clean vs Noisy")

plt.subplot(3, 2, 5)
plt.plot(ccCleanPeriodic, color='purple')
plt.title("Cross-Correlation - Clean vs Periodic")

plt.tight_layout()
plt.show()
