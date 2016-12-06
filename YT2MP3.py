import os
import sys
from pytube import YouTube
from moviepy import editor

yt = YouTube(sys.argv[1])
filename = ''.join(sys.argv[2])

print(sys.argv[1:])
print(sys.argv[1])
print(sys.argv[2])
#print(yt.get_videos())
print(yt.filename)

yt.set_filename(filename)

print(yt.filter('flv'))
video = yt.get('3gp', '240p')
video.download(os.path.abspath(os.curdir))


video = editor.VideoFileClip(os.path.abspath(os.curdir)+"/"+yt.filename+".3gp")
video.audio.write_audiofile(filename + ".mp3")