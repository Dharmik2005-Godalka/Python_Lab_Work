import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
fs = 500        # Sampling frequency
f = 5           # Frequency of the signal
t = np.linspace(0, 1, fs, endpoint=False)  # Time array 

# Create sine wave
sine_wave = np.sin(2 * np.pi * f * t)

# Create square wave
square_wave = signal.square(2 * np.pi * f * t)

# Plot
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t, sine_wave)
plt.title('Sine Wave (5 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, square_wave)
plt.title('Square Wave (5 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
