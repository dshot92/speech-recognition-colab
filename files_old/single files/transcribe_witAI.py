# https://github.com/wit-ai/pywit.git
# https://wit.ai/docs/http/20200513#post--speech-link

import sys
import json
import requests
import os.path
import speech_recognition as sr
from pydub import AudioSegment
import time # for delay
from wit import Wit

access_token = 'NZ53DR2SUADO2PBLJONJI3H4OZZDB3AD'
client = Wit(access_token)

path = './input'
list = os.listdir(path)

r = sr.Recognizer()

audio = AudioSegment.from_wav(path + '/' + str(list[0]))
offset = 15000 # 15000 == 15 seconds -- calculate in millisecond

for j in range(len(audio) / offset):
	t1 = j * offset #Works in milliseconds
	t2 = t1 + offset

	audio_segment = audio[t1:t2]
	audio_segment.export('./smith_small.wav', format="wav")

	with open('./smith_small.wav', 'rb') as f:
		resp = client.speech(f, {'Content-Type': 'audio/wav'})
        os.remove("./smith_small.wav")

	file_object = open('./output/witAI_transcribed.txt', 'a')
	file_object.write(str(resp['text']))
	file_object.close()

	print(str(resp['text']))
