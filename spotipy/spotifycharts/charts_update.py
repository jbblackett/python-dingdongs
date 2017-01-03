#Program by Jacob Blackett
#http://github.com/jbblackett/spotipy/spotifycharts/charts_update.py
# WORKS, JUST TAKES A WHILE!

#Improvements:
#-Add prints to know what stage program at
#-Make all artist images same size
#-Add more comments

import spotipy
import spotipy.util as util
import ftplib
import time as t

start = t.time()
errorlog = []
#ftp creds
print("Initialising FTP server credinitials...")
ip = "31.170.165.197"
port = 21
login = "u992204203"
password = ""

#Connect to spotify
print("Initialising spotify credinitials...")
token = util.prompt_for_user_token("monitorlad210",
                                   scope="playlist-read-private",
                                   client_id="f677c230b89246a3b43875be57390003",
                                   client_secret="670683077eed4d2883d5a211702f543d",
                                   redirect_uri="http://localhost:8888/callback")

s = spotipy.Spotify(auth=token)
user = "spotifycharts"

#Dictionary of charts
print("Initialising spotify chart dictionary...")
CHARTS = {"Global" : "37i9dQZEVXbMDoHDwVN2tF",
          "UnitedKingdom" : "37i9dQZEVXbLnolsZ8PSNw",
          "UnitedStates" : "37i9dQZEVXbLRQDuF5jeBp",
          "France" : "37i9dQZEVXbIPWwFssbupI",
          "Australia" : "37i9dQZEVXbJPcfkRz0wJ0",
          "Canada" : "37i9dQZEVXbKj23U1GF4IR",
          "Ecuador" : "37i9dQZEVXbJlM6nvL1nD1",
          "Finland" : "37i9dQZEVXbMxcczTSoGwZ",
          "Japan" : "37i9dQZEVXbKXQ4mDTEBXq",
          "Mexico" : "37i9dQZEVXbKXQ4mDTEBXq",
          "Spain" : "37i9dQZEVXbNFJfN1Vw8d9",
          "Sweden" : "37i9dQZEVXbLoATJ81JYXz"}

footer = """
</body>
</html>
"""

#Function to return the first part of html with given title
def getHeader(title):
    header = """
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <title>"""

    header += title

    header += """</title>
    </head>
    <body>
    <h1><a href="index.html">Spotify Charts</a></h1>
    <h2>Various spotify charts built using the python module <a href="https://github.com/plamere/spotipy">spotipy by plamere</a></h2>
    <h3><a href="http://github.com/jbblackett/python-dingdongs/spotipy/spotifycharts/charts_update.py">Source Code</a></h3>
    """
    return header

#Function to return list of tracks (in html) in given playlist id (country is just for heading)
def getChart(sid, countryname):
    global s
    #Initiate lines var, each line an item
    lines = []
    #Convert to spotify id
    spotifyid = "spotify:playlist:" + sid
    #Get chart
    chart = s.user_playlist(user, playlist_id=spotifyid)
    tracks = chart['tracks']
    chart_tracks = []

    #Get list of tracks
    for i, item in enumerate(tracks['items']):
        chart_tracks.append(item['track'])

    #Write header
    lines.append("<h3>" + countryname + " Top 50</h3>")

    #Write html
    lines.append('<div style="text-align:center;">\n')
    lines.append('<table style="margin:0px auto;" border="1px">\n')
    lines.append("<tr><td><h2>No.</h2></td><td><h2>Title</h2></td><td><h2>Artist</h2></td></tr>")
    for i in range(len(chart_tracks)):
        #Initialise artist
        artist_id = chart_tracks[i]['artists'][0]['id']
        artist_obj = s.artist(artist_id)
        artist_name = artist_obj['name']
        artist_img = artist_obj['images'][0]['url']

        #Initialise track name and link and preview url
        track_obj = chart_tracks[i]
        track_link = track_obj['external_urls']['spotify']
        track_name = track_obj['name']
        track_preview = track_obj['preview_url']

        lines.append('<tr>\n')
        lines.append('<td>' + str(i+1) + "</td>\n")
        lines.append('<td><br><a href="' + track_link + '">' + track_name + '</a>\n')
        if track_preview:
            lines.append('<br><br><audio controls><source src="' + track_preview + '" type="audio/mp3"></audio><br></td>\n')
        else:
            lines.append('</td>')
        lines.append('<td><a href="#' + artist_name + '">' + artist_name + "</a>\n")
        lines.append('<br><img src="' + artist_img + '" height="50" width="50"></td>\n')
        lines.append('</tr>\n')

    lines.append("</table>")
    lines.append("</div>")
    #Write list of artists
    for i in range(len(chart_tracks)):
        artist_id = chart_tracks[i]['artists'][0]['id']
        artist_obj = s.artist(artist_id)
        artist_name = artist_obj['name']
        lines.append("<h2 id='" + artist_name + "'>" + artist_name + "</h2>\n")
        artist_link = artist_obj['external_urls']['spotify']
        lines.append('<p><a href="' + artist_link + '">Artist Link</a></p>\n')
        artist_followers = artist_obj['followers']['total']
        lines.append('<p>Followers: ' + str(artist_followers) + '</p>\n')
        try:
            artist_img = artist_obj['images'][2]['url']
            lines.append('<img src="' + artist_img + '">\n')
        except:
            print("Could not get image for " + artist_name)

    #send back list of html lines
    return lines

#Initiate index.html
print("Creating file index.html...")
file = open("index.html", "w+")
file.write(getHeader("Home"))

#Display list of avaliable charts with links
print("Adding links to index.html...")
file.write("<br><br>\n")
for country, sid in CHARTS.items():
    file.write('<p><a href="' + country.lower() + '.html">' + country + '</a></p>\n')
file.close()

#loop to create html file for each country
for country, sid in CHARTS.items():
    print("Creating html file for " + country + "...")
    #Create file
    file = open(country.lower() + ".html", "w+")
    #Write header with country title
    file.write(getHeader(country))
    #Write the charts
    lines = getChart(sid,country)
    #Write each html line to file
    for i in range(len(lines)):
        try:
            file.write(lines[i] + "\n")
        except:
            errorlog.append("E")
    file.close()

print(str(len(errorlog)) + " unicode errors.")

#Upload all files to FTP server
#Connect to FTP server
print("Connecting to FTP server...")
ftp = ftplib.FTP()
ftp.connect(ip,port)
ftp.login(login,password)
ftp.cwd("spotify")

#Upload index.html
print("Uploading files...")
up = open("index.html", "rb")
print(ftp.storbinary("STOR " + "index.html",up))
up.close()
#Upload stylesheet.css
up = open("stylesheet.css", "rb")
print(ftp.storbinary("STOR " + "stylesheet.css",up))
up.close()

#Upload country charts
for country, sid in CHARTS.items():
    filename = country.lower() + ".html"
    up = open(filename, "rb")
    print(ftp.storbinary("STOR " + filename,up))
    up.close()
    t.sleep(1)
end = t.time()
print("Completed in " + str(end-start) + " seconds.")
