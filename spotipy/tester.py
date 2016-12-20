import spotipy
import spotipy.util as util

username = "#"
client = "#"
secret = "#"
redirect = "#"

s = None
charttop50 = []

CHARTIDS = {"France":"37i9dQZEVXbIPWwFssbupI",
            "Global":"37i9dQZEVXbMDoHDwVN2tF",
            "United Kingdom":"37i9dQZEVXbLnolsZ8PSNw",
            "United States":"37i9dQZEVXbLRQDuF5jeBp"}

def auth(scope):
    global s
    token = util.prompt_for_user_token(username,
                                   scope=scope,
                                   client_id=client,
                                   client_secret=secret,
                                   redirect_uri=redirect)

    s = spotipy.Spotify(auth=token)


def getSavedTracks():
    global s
    auth("user-library-read")
    savedtracks = s.current_user_saved_tracks()
    for item in savedtracks['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
        


def getArtistTop10():
    global s
    auth(None)
    results = s.search(q=input("Artist: "),type='artist')
    topartistid = results['artists']['items'][0]['id']
    topartistname = results['artists']['items'][0]['name']

    toptracks = s.artist_top_tracks(topartistid)
    print()
    print("Top tracks for " + topartistname)
    i=1
    for track in toptracks['tracks'][:20]:
        print("Track #" + str(i) + ": " + track['name'])
        i += 1

def getTopTracks():
    global s
    auth("user-top-read")
    s.trace = False

    results = s.current_user_top_tracks(time_range='long_term', limit=100)
    
    for i, item in enumerate(results['items']):
        print(str(i+1) + " " + item['name'] + ' - ' + item['artists'][0]['name'])
    print()

def getTopArtists():
    global s
    auth("user-top-read")
    s.trace = False

    results = s.current_user_top_artists(time_range='long_term', limit=100)
    
    for i, item in enumerate(results['items']):
        print(str(i+1) + " " + item['name'])

def getArtistAlbums():
    global s
    auth(None)
    
    results = s.search(q=input("Artist: "),type='artist')
    topartistid = "spotify:artist:" + results['artists']['items'][0]['id']
    
    print(topartistid)
    results = s.artist_albums(topartistid, album_type='album')
    albums = results['items']

    while results['next']:
        results = s.next(results)
        albums.extend(results['items'])
        
    for album in albums:
        print(album['name'])

def createHTMLFile():
    global charttop50
    file = open("chart.html", "w+")
    file.write("<html>")
    file.write("\n")
    for i in range(len(charttop50)):
        link = charttop50[i]['external_urls']['spotify']
        name = charttop50[i]['name'] + " - " + charttop50[i]['artists'][0]['name']
        file.write('<p><a href="' + link + '">' + name + '</a></p>')
        file.write("\n")
    file.write("</html>")
    file.write("\n")
    file.close()

def getTracksInPlaylist():
    global s, charttop50
    auth("playlist-read-private")

    chart = s.user_playlist("spotifycharts", playlist_id="spotify:playlist:" + CHARTIDS[input("Country: ")])
    print(chart['name']+" (" + str(chart['tracks']['total']) + " tracks):")
    
    tracks = chart['tracks']
    for i, item in enumerate(tracks['items']):
        track = item['track']
        #print(str(i+1) + ". " + track['name'] + " - " + track['artists'][0]['name'])
        charttop50.append(track)
    if input("Create HTML File? ").lower() == "yes":
        createHTMLFile()
