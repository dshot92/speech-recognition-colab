#!/usr/bin/env python3

import speech_recognition as sr
import json

# obtain path to "english.wav" in the same folder as this script
from os import path
from pydub import AudioSegment

# files                                                                         
src = "input.mp3"
dst = "output.wav"

# convert wav to mp3                                                            
totrasn = AudioSegment.from_mp3(src)
totrasn.export(dst, format="wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(dst) as source:
    audio = r.record(source)  # read the entire audio file
    
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    f = open("trascribed.txt", "a")
    f.write( "Result: \n" + str(r.recognize_google(audio, language="it-IT", show_all=True)) )		#ITALIAN
    #f.write( "Result: \n" + str(r.recognize_google(audio, show_all=True)) ) 			#ENGLISH-US 
    f.close()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
