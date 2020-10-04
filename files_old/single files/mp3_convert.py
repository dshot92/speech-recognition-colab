import os
import sys
from os import path
from pydub import AudioSegment

path = './mp3_input'
list = os.listdir(path)
for file in list:
    print('Converting file : ' + file)
    src = path + '/' + file
    sound = AudioSegment.from_mp3(src)
    head, sep, tail = file.partition('.')
    sound.export('./input/' + head + '.wav', format="wav")
