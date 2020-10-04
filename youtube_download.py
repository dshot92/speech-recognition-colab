# https://github.com/nficano/pytube
import os
import pytube

print("Enter YouTube video url: ")
url = str(input())

if not os.path.exists('input'):
    os.makedirs('input')

input_folder = os.path.join(os.getcwd(), "input")

try:
    ytd = pytube.YouTube(url)
    print('\nVideo Title:')
    name = ytd.title
    print(ytd.title)
    print("\n..Downloading..")
    ytd = pytube.YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(input_folder)
    print('\n # Done # ')

except pytube.exceptions.RegexMatchError as e:
    print('Error : {}'.format(e))
