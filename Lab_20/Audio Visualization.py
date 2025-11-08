import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

audio, sample = sf.read(r"C:\Users\Dharmik\Downloads\audio_5.wav")
sf.write(r"C:\Users\Dharmik\Downloads\audio_5.wav", audio, sample)

time = np.arange(0, len(audio)) / sample

plt.plot(time, audio)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.show()
