from os import path
from pydub import AudioSegment

# Cutting audio into 5 minutes slices

offset = 300000 # 300000 == 5 minutes
t1 = 0 
t2 = offset
for i in range(6):
    t1 = i * offset #Works in milliseconds
    t2 = t1 + offset
    #print(t1,t2)
    newAudio = AudioSegment.from_wav("ISW_a_complete.wav")
    newAudio = newAudio[t1:t2]
    newAudio.export('test/ISW_a_'+ str(i) + '.wav', format="wav") #Exports to a wav file in the current path.
