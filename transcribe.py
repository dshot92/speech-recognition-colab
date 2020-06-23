#!/usr/bin/env python3
import os
import sys
import time # for delay
import json
import datetime
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
path_input = os.getcwd() + os.sep +  'input'
path_output = os.getcwd() + os.sep +  'output'

list = os.listdir(path_input)
if len(list) < 1 :
    print('No files to transcribe!')
    sys.exit()

# list of file in input folder
print('\nSelect file to transcribe: ')
for i in range(len(list)):
    print(str(i) + ' : ' + list[i])

#get input from user
file = int(input())

file = list[file]

# get audiofile into usable form
audio = AudioSegment.from_file(os.path.join(path_input, str(file)))
offset = 15000 # 15000 == 15 seconds -- calculate in millisecond

# initialize recognizer
r = sr.Recognizer()
print('\nSelect platform for transcribing: \n0 : Google\n1 : Wit.AI')

# select APIs to use
method = int(input())

languages = ['en-US', 'it-IT']
print('\nSelect language transcribing: \n0 : English\n1 : Italian')
language = int(input())
language = languages[language]

parts = 1 + (len(audio) // offset)
for j in range(parts):
    # get intervals of 15 from audio data
    t1 = j * offset
    t2 = t1 + offset
    audio_segment = audio[t1:t2 + 1000]

    audio_segment.export(os.path.join(path_input, 'temporary.wav') , format="wav")

    start = str(datetime.timedelta(seconds=t1 / 1000))
    end = str(datetime.timedelta(seconds=t2 / 1000))
    print('Part {} of {} \t [ {}s : {}s ]'.format(j+1,parts, start,end ))
    if method == 0:
        try:
            with sr.AudioFile( os.path.join(path_input, 'temporary.wav')) as source:
                aux = r.record(source)  # read the entire audio file

            # call to google APIs
            data = r.recognize_google(aux, language=language, show_all=False) # English

            file_object = open(os.path.join(path_output, file) + '_google.txt' , 'a')
            file_object.write('\n[ ' + str(datetime.timedelta(seconds=t1 / 1000)) + 's : ' + str(datetime.timedelta(seconds=t2 / 1000)) + 's ]\n')
            if str(data)[-1] == ' ':
                file_object.write(str(data))
            else:
                file_object.write(str(data) + ' ')
            file_object.close()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # 1 = Wit.AI
    elif method == 1:
        with open(os.path.join(path_input, 'temporary.wav'), 'rb') as f:
            # call to Wit.AI APIs
            resp = client.speech(f, {'Content-Type': 'audio/wav'})

        file_object = open(os.path.join(path_output, file + '_witAI.txt') , 'a')
        file_object.write('\n[ ' + str(datetime.timedelta(seconds=t1 / 1000)) + 's : ' + str(datetime.timedelta(seconds=t2 / 1000)) + 's ]\n')
        if str(resp['text'])[-1] == ' ':
            file_object.write(str(resp['text']))
        else:
            file_object.write(str(resp['text']) + ' ')
        file_object.close()

    #delete aux files of 15 seconds
    os.remove(os.path.join(path_input, 'temporary.wav'))

# Last step
print('Done')

