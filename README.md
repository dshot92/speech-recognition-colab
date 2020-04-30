# Speech Recognition

Quick files ready to get an mp3 input of 5 minutes and output it in its transcribed form.

Will automaticly convert file into wav and then transcribe it.
Google is really amazing in understanding, both english and italian but has a max free cap of 60 minutes/month.
https://cloud.google.com/speech-to-text

Pocket Sphinx works offline, but requires a prebuild model for each language.
i've added an italian model and the instruction on how to use it, but the accuracy is that great.

Based on 

```
https://github.com/Uberi/speech_recognition
```

------



### Install

```
git clone https://github.com/dshot92/speechrecognition.git
cd speechrecognition
git clone https://github.com/Uberi/speech_recognition.git
cd speech_recognition
python3 setup.py install
sudo pip3 install pydub
sudo pip3 install pyaudio
sudo apt install ffmpeg libavcodec-extra-53
pip3 install pocketsphinx
```

### Usage

Copy mp3 files into main folder and change src and dst strings in the script files. 

##### Scripts

```
python3 trascribe_google.py 	# Google Cloud - connection required

python3 trascribe_sphinx.py  	# Pocket Sphinx - Offline
```



------



### Pocket Sphinx Italian setup:

```
sudo apt install unzip
sudo unzip ./PocketSphinx_Setup/it-IT.zip
sudo mv ./pocketsphinx-data /usr/local/lib/python3.8/dist-packages/speech_recognition/pocketsphinx-data

```

For references:

```
https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst
```



