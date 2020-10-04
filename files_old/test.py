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
path = '/input/'

print(os.path.abspath(os.getcwd()) + path)

list = os.listdir(os.path.abspath(os.getcwd()) + path)
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
audio = AudioSegment.from_file( os.path.abspath(os.getcwd()) + path + str(file))

print(audio.duration_seconds)

#audio.export( os.path.abspath(os.getcwd()) + '/test.wav', format="wav")
