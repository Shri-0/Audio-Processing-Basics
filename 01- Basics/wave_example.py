# Audio file formats
# .mp3
# .flac
# .wav

import wave

# Audio signal parameters
# - number of channels
# - sample width
# - framerate/sample_rate: 44,100Hz
# - number of frames
# - values of a frame


obj = wave.open("carey.wav", "rb")

print("number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getnchannels())
print("number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()

print(t_audio)

frames = obj.readframes(-1)  # will read all frames
print(type(frames), type(frames[0]))
print(len(frames)/2)

obj.close()

obj_new = wave.open("shri_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()
