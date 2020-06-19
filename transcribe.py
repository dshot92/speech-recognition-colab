#!/usr/bin/env python3
import os
import sys
import time # for delay
import json
import requests
import speech_recognition as sr
from os import listdir
from wit import Wit
from pydub import AudioSegment

# wit.ai token api
access_token = 'Enter Wit.AI token Here'
access_token = 'NZ53DR2SUADO2PBLJONJI3H4OZZDB3AD'

client = Wit(access_token)

# get list of file in input folder
path = './input'
list = os.listdir(path)
if len(list) < 1 :
    print('No files to transcribe!')
    sys.exit()

# list of file in input folder
print('\nSelect file to transcribe: ')
for i in range(len(list)):
    print(str(i) + ' : ' + list[i])

#get input from user
file = int(input())

#if not wav file, converts it to wav
if list[file].rsplit('.', 1)[1] != 'wav':
    sound = AudioSegment.from_file(path + '/' + list[file], list[file].rsplit('.', 1)[1])
    sound.export('./input/' + list[file].rsplit('.', 1)[0] + '.wav', format="wav")
    file = list[file].rsplit('.', 1)[0] + '.wav'
else:
    file = list[file]

# get audiofile into usable form
audio = AudioSegment.from_wav(path + '/' + str(file))
offset = 15000 # 15000 == 15 seconds -- calculate in millisecond

# initialize recognizer
r = sr.Recognizer()
print('\nSelect platform for transcribing: \n0 : Google\n1 : Wit.AI')

# select APIs to use
method = int(input())
parts = 1 + (len(audio) // offset)
for j in range(parts):

    # get intervals of 15 from audio data
    t1 = j * offset
    t2 = t1 + offset
    audio_segment = audio[t1:t2]
    audio_segment.export('./aux.wav', format="wav")

    print('Part {} of {}'.format(j+1, parts))
    # 0 = Google
    if method == 0:
        try:
            with sr.AudioFile('./aux.wav') as source:
                aux = r.record(source)  # read the entire audio file

            # call to google APIs
            data = r.recognize_google(aux, language="en-US", show_all=False) # English
            # data = r.recognize_google(aux, language="it-IT", show_all=False) # Italian

            file_object = open('./output/' + file + '_google.txt', 'a')
            file_object.write(str(data))
            file_object.close()
            # print(str(data))

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # 1 = Wit.AI
    elif method == 1:
        with open('./aux.wav', 'rb') as f:
            # call to Wit.AI APIs
            resp = client.speech(f, {'Content-Type': 'audio/wav'})

        file_object = open('./output/' + file + '_witAI.txt', 'a')
        file_object.write(str(resp['text']))
        file_object.close()
        # print(str(resp['text']))

    #delete aux files of 15 seconds
    os.remove("./aux.wav")

# Last step
print('Done')
