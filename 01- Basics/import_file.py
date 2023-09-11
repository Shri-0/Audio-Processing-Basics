from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

audio = audio + 6  # increase the volume by 6db

audio = audio * 2  # repeat the clip twice

audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")
