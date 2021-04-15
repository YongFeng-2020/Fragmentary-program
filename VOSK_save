#!/usr/bin/env python3
# 实现从麦克风读入音频存到本地并输出语音的文字内容

import pyaudio
from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import numpy as np
import json

Model_path = '/home/zyf-903/others/model'
WAVE_OUTPUT_FILENAME = "output.wav"
CHUNK = 8000
RATE = 16000
RECORD_SECONDS = 5
SetLogLevel(0)

model = Model(Model_path)
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
stream.start_stream()
frames = []

while True:
    data = stream.read(4000)
    data2 = data
    # p.terminate()
    if len(data) == 0:
        frames.clear()
        break
    if rec.AcceptWaveform(data):
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(RATE)
        wf.writeframes(np.array(frames).tostring())
        wf.close()
        frames.clear()
        result = rec.Result()
        print(result)

    else:
        frames.append(data2)
        print(rec.PartialResult())

print(rec.FinalResult())
