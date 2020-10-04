#!/usr/bin/env python3
import os
import sys
import time  # for delay
import datetime
import speech_recognition as sr
from os import listdir
import pydub
from pydub import AudioSegment

# get list of file in input folder
path_input = os.getcwd() + os.sep + 'input'
path_output = os.getcwd() + os.sep + 'output'

# pydub.AudioSegment.ffmpeg = "C:/ffmpeg"

list = os.listdir(path_input)
if len(list) < 1:
    print('No files to transcribe!')
    sys.exit()

# list of file in input folder
print('\nSelect file to transcribe: ')
for i in range(len(list)):
    print(str(i) + ' : ' + list[i])

# get input from userò
file_name = int(input())
print(file_name)
file_name = list[file_name]

# get audiofile into usable form
audio = AudioSegment.from_file(os.path.join(path_input, str(file_name)))
offset = 3000  # 15000 == 15 seconds -- calculate in millisecond

# initialize recognizer
r = sr.Recognizer()

# Languages List
# http://www.lingoes.net/en/translator/langcode.htm

languages = ['en-US', 'it-IT']
print('\nSelect language transcribing:')
for j in range(len(languages)):
    print('{} : {}'.format(j, languages[j]))
language = int(input())
print(language)
language = languages[language]

parts = 1 + (len(audio) // offset)
for j in range(parts):
    # get intervals of 15 from audio data
    t1 = j * offset
    t2 = t1 + offset
    audio_segment = audio[t1:t2 + 1000]

    audio_segment.export(os.path.join(
        path_input, 'temporary.wav'), format="wav")

    start = str(datetime.timedelta(seconds=t1 / 1000))
    end = str(datetime.timedelta(seconds=t2 / 1000))
    print('Part {} of {} \t [ {}s : {}s ]'.format(j+1, parts, start, end))
    try:
        with sr.AudioFile(os.path.join(path_input, 'temporary.wav')) as source:
            aux = r.record(source)  # read the entire audio file

        # call to google APIs
        data = r.recognize_google(
            aux, language=language, show_all=False)  # English

        file_object = open(os.path.join(
            path_output, file_name) + '_google.srt', 'a')
        #file_object.write('\n[ ' + str(datetime.timedelta(seconds=t1 / 1000)) + 's : ' + str(datetime.timedelta(seconds=t2 / 1000)) + 's ]\n')
        if str(data)[-1] == ' ':
            file_object.write('\n\n' + str(j) + '\n' +
                              '{} --> {}'.format(start, end) + '\n' + str(data))
        else:
            file_object.write(
                '\n\n' + str(j) + '\n' + '{} --> {}'.format(start, end) + '\n' + str(data) + ' ')
        file_object.close()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    # delete aux files of 15 seconds
    os.remove(os.path.join(path_input, 'temporary.wav'))
# Last step
print('Done')
