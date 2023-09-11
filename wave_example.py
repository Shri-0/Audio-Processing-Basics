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
