import os, io
import webbrowser
from urllib import request

for i in range(12):

    videos = []
    f = open("youtubeVidID.txt", 'r')
    videos = f.read().split('\n')[600 + 50*i:650+50*i]
    listOfVideos = "http://www.youtube.com/watch_videos?video_ids=" + ",".join(videos)

    response = request.urlopen(listOfVideos)
    playListLink = response.geturl().split('list=')[1]

    # edit playlist with this URL
    playListURL = "https://www.youtube.com/playlist?list=" + playListLink 

    # or start playing from first to last with this one
    playNowURL = "https://www.youtube.com/watch?v=" + videos[0] + "&list=" + playListLink

    print(playListURL)
