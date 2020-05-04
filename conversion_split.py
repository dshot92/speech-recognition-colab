import os.path
import sys
import speech_recognition as sr
from pydub import AudioSegment
import time # for delay

# Transcribe from google APIs

dir = "../20_minutes_slice/test"
onlyfiles = next(os.walk(dir))[2] #dir is your directory path as string
print ('Found ' + str(len([name for name in os.listdir(dir)])) + ' files to transcribe' )

r = sr.Recognizer()

result = [] # Output visualization

for i in range(len(onlyfiles)):
    
    time.sleep(10) # seconds
    
    print('Processing File: ' + str(i))
    file_wav = dir + '/ISW_a_'+ str(i) + '.wav'
    
    # use the audio file as the audio source
    with sr.AudioFile(file_wav) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        
        file = open(dir + '/Text/ISW_a_'+ str(i) + '.txt',"w+")
        file.write(str(r.recognize_google(audio, language="it-IT") )) #ITALIAN
        file.close()
        
        result.append([i, True])

        #print( r.recognize_google(audio, show_all=True) ) #ENGLISH-US 

    except sr.UnknownValueError:
        result.append([i, False])
        print('File_'+ str(i) + ' - Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

        
for res in result:
    print(res)
