import soundfile as sf

audio, sample = sf.read(r"C:\Users\Dharmik\Downloads\audio_5.wav")
sf.write(r"C:\Users\Dharmik\Downloads\new_audio_5.wav", audio, sample)

print("Sample rate:", sample)
print("Audio data shape:", audio.shape)
