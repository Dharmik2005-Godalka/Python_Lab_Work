import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 20
t_continuous = np.linspace(0, 1, 1000)
t_discrete = np.arange(0, 1, 1/fs)

f = 5
continuous_signal = np.sin(2 * np.pi * f * t_continuous)
discrete_time_signal = np.sin(2 * np.pi * f * t_discrete)

# Discrete Amplitude
num_levels = 4
discrete_amplitude_signal = np.round(continuous_signal * (num_levels/2)) / (num_levels/2)

# Discrete Time + Amplitude
discrete_time_amplitude_signal = np.round(discrete_time_signal * (num_levels/2)) / (num_levels/2)

# Plot
plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(t_continuous, continuous_signal)
plt.title('Continuous-Time Signal')

plt.subplot(4, 1, 2)
plt.stem(t_discrete, discrete_time_signal, use_line_collection=True)
plt.title('Discrete-Time Signal')

plt.subplot(4, 1, 3)
plt.plot(t_continuous, discrete_amplitude_signal, drawstyle='steps-pre')
plt.title('Discrete-Amplitude Signal')

plt.subplot(4, 1, 4)
plt.stem(t_discrete, discrete_time_amplitude_signal, use_line_collection=True)
plt.title('Discrete-Time & Amplitude Signal')

plt.tight_layout()
plt.show()
