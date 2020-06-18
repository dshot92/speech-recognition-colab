

# Speech Recognition

Automatization of already written tools to transcibe audio files.

Autoconverts audio files to wav for simpler handling while transcribe.

Utilizes Google Speech-to-text and Wit.AI  APIs.

Google is really amazing in understanding, both english and italian but has a max free cap of 60 minutes/month.
https://cloud.google.com/speech-to-text

Wit.AI is free but is not as precise as the google alternative

https://wit.ai/



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
pip3 install pytube3
```

### Usage

Insert yours Wit.AI token if you want to use these APIs into the transcribe.py file

Copy audio files into input folder and then run:

```
python3 transcribe.py
```

The script will prompt which file to transcribe and automatically convert them to wav format without deleting the original files.

To download a video from Youtube use the script

```
python3 youtube_download.py
```

Enter the video url and the audio file of maximum quality allowed will automatically be downloaded into the input folder ready to be transcribed.