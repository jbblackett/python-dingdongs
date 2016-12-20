import spotipy
import spotipy.util as util
import ftplib
import time as t

errorlog = []
#ftp creds
ip = ""
port = 0
login = ""
password = ""

#Connect to spotify
token = util.prompt_for_user_token("",
                                   scope="",
                                   client_id="",
                                   client_secret="",
                                   redirect_uri="")

s = spotipy.Spotify(auth=token)
user = "spotifycharts"

#Dictionary of charts
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
    <h2>Various spotify charts built using the python module <a href="https://github.com/plamere/spotipy">spotipy by plamere</a>.
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
    for i in range(len(chart_tracks)):
        track_link = chart_tracks[i]['external_urls']['spotify']
        #track_link = "spotify:track:" + sid
        track_display = str(i+1) + ". " + chart_tracks[i]['name'] + " - " + chart_tracks[i]['artists'][0]['name']
        lines.append('<p><a href="' + track_link + '" target="_blank">' + track_display + '</a></p>')
    #send back list of html lines
    return lines
   
    

#Initiate index.html
file = open("index.html", "w+")
file.write(getHeader("Home"))


#Display list of avaliable charts with links
file.write("<br><br>\n")
for country, sid in CHARTS.items():
    file.write('<p><a href="' + country.lower() + '.html">' + country + '</a></p>\n')
file.close()

#loop to create html file for each country
for country, sid in CHARTS.items():
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
ftp = ftplib.FTP()
ftp.connect(ip,port)
ftp.login(login,password)
ftp.cwd("spotify")

#Upload index.html
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
