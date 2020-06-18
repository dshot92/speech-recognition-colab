#!/usr/bin/env python3

import speech_recognition as sr

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
    
# recognize speech using Sphinx

try:
    #print("Sphinx thinks you said " + r.recognize_sphinx(audio, language="it-IT"))  #ITALIAN
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))  #ENGLISH-US
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
