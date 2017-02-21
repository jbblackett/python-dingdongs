import spotipy
import spotipy.util as util
import time

tracknames = []
data = []
processed = []
options = ['Danceability',
           'Energy',
           'Loudness',
           'Speechiness',
           'Acousticness',
           'Instrumentalness',
           'Liveness',
           'Valence',
           'Tempo',
           'Length']

options_s = ['danceability',
           'energy',
           'loudness',
           'speechiness',
           'acousticness',
           'instrumentalness',
           'liveness',
           'valence',
           'tempo',
           'duration_ms']

token = util.prompt_for_user_token("monitorlad210",
                                   scope="playlist-read-private",
                                   client_id="f677c230b89246a3b43875be57390003",
                                   client_secret="c200e543ad1d43ac9d092ecb9db5135c",
                                   redirect_uri="http://localhost:8888/callback")

s = spotipy.Spotify(auth = token)

def toTime(ms):
    sec = round(ms / 1000,0)
    return(str(time.strftime('%M:%S', time.gmtime(sec))))

while True:
    try:
        alb_id = s.search(input("Album: "),limit=1,type='album')['albums']['items'][0]['id']
        break
    except:
        print('Album not found.')
        
alb_obj = s.album(alb_id)
tracks = s.album_tracks(alb_id, limit=50)['items']

print('\nAlbum found.')
print('\nTitle:')
print("   " + alb_obj['name'])
print('Artist(s):')
for artist in alb_obj['artists']:
    print("   " + artist['name'])
print('Number of Tracks:')
print("   " + str(len(tracks)) + "\n")
    
for i in range(len(options)):
    print(str(i+1) + ". " + options[i])
option = input("\nEnter a characteristic to order by: ")

option = options_s[int(option)-1]

for track in tracks:
    try:
        name = track['name']
        t_id = track['id']
        d = s.audio_features(t_id)[0][option]
        tracknames.append(name)
        data.append(d)
    except:
        pass

processed = sorted(zip(data,tracknames), reverse=True)

for item in processed:
    if option == "Length":
        print(item[1] + " - " + toTime(item[0]))
    else:
        print(item[i])
