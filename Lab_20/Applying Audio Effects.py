from pydub import AudioSegment 

audio = AudioSegment.from_file(r"C:\Users\Dharmik\Downloads\audio_5.wav")

audio1 = audio.fade_in(2000)

audio1.export(r"C:\Users\Dharmik\Downloads\audio_5_fadein.wav", format='wav')

print("Audio effect saved successfully!")
