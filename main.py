from pytube import YouTube
from sys import argv

link = "https://www.youtube.com/watch?v=m3aVgzU45uU"
yt = YouTube(link)

print('Title: ', yt.title)
print('View: ', yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('D:\Python\Projects\Python Projects\Youtube_Video_Downloader\Download')
