import spotipy
import spotipy.util as util
import time as t

token = util.prompt_for_user_token("",
                                   scope="playlist-modify-private",
                                   client_id="",
                                   client_secret="",
                                   redirect_uri="http://localhost:8888/callback")

s = spotipy.Spotify(auth=token)

def getTrackID(name):
    try:
        sresults = s.search(name, type='track', limit=1)
        return sresults['tracks']['items'][0]
    except:
        return False

user = ''
tracks = []
ids = []
title = input("Playlist name: ")

cont = True
while cont:
    inp = input("\nTrack name: ")
    track = getTrackID(inp)
    if not track:
        print('\nTrack not found.')
    else:
        name = track['name']
        artist = track['artists'][0]['name']
        print('\nTitle: ' + name)
        print('Artist: ' + artist)

        inp = (input('\nAdd to playlist? '))
        if inp.lower() == 'yes':
            tracks.append(track)
            ids.append(track['id'])
        
    if (input("\nAnother Track? ")).lower() == "no":
        cont = False 

if tracks:
    print('\n' + title + ':')
    for track in tracks:
        print('   ' + track['name'] + ' - ' + track['artists'][0]['name'])
    if (input('\nCreate playlist? ')).lower() == 'yes':
        print('Creating playlist...')
        playlist = s.user_playlist_create(user, title, public=False)['id']
        print('Building playlist...')
        s.user_playlist_add_tracks(user, playlist, ids, position=None)
        print('Playlist built.')
        
else:
    print('\nNo tracks to add.')
