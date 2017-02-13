import spotipy

def printArtists(track):
    
    print('\n'+track['name']+'\n')

    for artist in track['artists']:
        print(artist['name'])


s = spotipy.Spotify()

#Get track obj
songInp = input("Track: ")
data = s.search(songInp, limit=1, type='track')
try:
    track = s.track(data['tracks']['items'][0]['id'])
    printArtists(track)
except:
    print("Track not found.")
