#Import mixer to play audio
from pygame import mixer as m
#Import urllib requests to download preview
import urllib.request
#Import spotipy to find song and get preview url
import spotipy
#Import time to wait 30s between songs
import time as t
#Import os to check if prev already downloaded
import os.path


def playPrev(file, name, artist):
    m.init()
    try:
        m.music.load(file)
        m.music.play()
        print("Playing " + name + " by " + artist + "...")
    except:
        print("Cound not play " + name)

def downloadPrev(url, filename):
    if not os.path.isfile("cache\\"+filename):    
        try:
            print("")
            filesize = urllib.request.urlopen(url).length
            print("Downloading track '" + filename + "' from '" + url + "' (" + str(round(filesize/1000)) + "KB)")
            print("")
            urllib.request.urlretrieve(url, "cache\\" + filename)
        except:
            print('Cound not download preview.')

def findSong(searchvalue):
    sresults = s.search(searchvalue, type = 'track', limit=1)
    track_obj = sresults['tracks']['items'][0]
    return track_obj

    
#Connect to spotify
s = spotipy.Spotify()

while True:
    #Ensure song input not empty
    song = None
    while not song:
        song = input("Song: ")
    if not (song.lower() == "same"):

        track_obj = findSong(song)
        filename = track_obj['id'] + '.mp3'
        track_url = track_obj['preview_url'] + '.mp3'

        #Download prev to cache
        downloadPrev(track_url, filename)

        track_name = track_obj['name']
        track_artist = track_obj['artists'][0]['name']

        if track_obj['explicit']:
            input("This track contains explicit language. Press enter to continue.")
    #Play prev
    playPrev("cache\\"+filename, track_name, track_artist)

    t.sleep(30)

