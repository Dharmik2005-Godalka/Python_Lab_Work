import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
fs = 500
f = 5
t = np.linspace(0, 1, fs, endpoint=False)

# Triangular wave
triangular_wave = signal.sawtooth(2 * np.pi * f * t, 0.5)

# Ramp (sawtooth) wave
ramp_signal = signal.sawtooth(2 * np.pi * f * t)

# Plot
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t, triangular_wave)
plt.title('Triangular Wave (5 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, ramp_signal)
plt.title('Ramp Signal (5 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
