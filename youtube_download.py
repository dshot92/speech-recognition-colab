# https://github.com/nficano/pytube
import shutil
import pytube

print("Enter YouTube video url: ")
url = str(input())

print("..Downloading..")
try:
    ytd = pytube.YouTube(url).streams.filter(only_audio=True).first().download()

    try:
        shutil.move(ytd, './input/')
        print('Done')
    except shutil.Error as e:
        print('{}'.format(e))

except pytube.exceptions.RegexMatchError as e:
    print('Error : {}'.format(e))
