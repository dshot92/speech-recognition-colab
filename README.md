# Speech Recognition Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dshot92/speech-recognition-colab/blob/master/Speech_Recognition_Colab.ipynb)

Automatization of already written tools to transcribe audio files.

Auto converts audio files to wav for simpler handling while transcribe.

Utilizes Google Speech-to-text.

Google is really amazing in understanding, both English and Italian.
https://cloud.google.com/speech-to-text

Based on

```
https://github.com/Uberi/speech_recognition
```

------



### Install

```pip install -r requirements.txt```

If using conda:

```conda install -c conda-forge ffmpeg```


### Usage

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

------

### Jupyter Install

#### For Python 3

```
pip3 install --upgrade --force-reinstall --no-cache-dir jupyter
```



------

TODO:

- [ ] impement https://stackoverflow.com/questions/36458214/split-speech-audio-file-on-words-in-python