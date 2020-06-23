# https://github.com/nficano/pytube
import pytube

print("Enter YouTube video url: ")
url = str(input())

try:
    ytd = pytube.YouTube(url)
    print('\nVideo Title:')
    print(ytd.title)
    print("\n..Downloading..")
    ytd = pytube.YouTube(url).streams.filter(only_audio=True).first().download('./input')
    print('\n # Done # ')

except pytube.exceptions.RegexMatchError as e:
    print('Error : {}'.format(e))
