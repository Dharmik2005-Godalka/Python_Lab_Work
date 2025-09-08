import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
fs = 500
t = np.linspace(-1, 1, fs, endpoint=False)

# 1. Unit Step Signal
unit_step = np.heaviside(t, 1)

# 2. Unit Impulse Signal
unit_impulse = np.zeros_like(t)
unit_impulse[fs//2] = 1

# 3. Ramp Signal
ramp_signal = signal.sawtooth(2 * np.pi * t, 1)

# 4. Sine Wave
sine_wave = np.sin(2 * np.pi * 5 * t)

# 5. Cosine Wave
cosine_wave = np.cos(2 * np.pi * 5 * t)

# 6. Exponential Signal
exponential_signal = np.exp(t)

# 7. Triangular Wave
triangular_wave = signal.sawtooth(2 * np.pi * 5 * t, 0.5)

# 8. Square Wave
square_wave = signal.square(2 * np.pi * 5 * t)

# Plot
plt.figure(figsize=(12, 12))

signals = [unit_step, unit_impulse, ramp_signal, sine_wave,
           cosine_wave, exponential_signal, triangular_wave, square_wave]
titles = ['Unit Step', 'Unit Impulse', 'Ramp', 'Sine Wave',
          'Cosine Wave', 'Exponential', 'Triangular', 'Square']

for i in range(8):
    plt.subplot(4, 2, i+1)
    plt.plot(t, signals[i])
    plt.title(titles[i])
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
