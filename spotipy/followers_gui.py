import tkinter
from tkinter import CENTER
import spotipy
from time import sleep

#Connect to spotify
s = spotipy.Spotify()

def getFollowers(artist_obj):
    #Function to return int number of followers for an artist
    artist_name_label.config(text= artist_obj['name'])
    followers_label.config(text = str(artist_obj['followers']['total']))
    #inp_artist_butt.place_forget()
    # while True:
    #     #crashes for some reason
    #     sleep(5)
    #     artist_name_label.config(text= artist_obj['name'])
    #     followers_label.config(text = str(artist_obj['followers']['total']))

def getArtist():
    #Function to search for most relevant artist from given text in text box
    search = inp_artist_ent.get()
    #Only search if text box not blank
    if search:
        results = s.search(search,type='artist')
        artist = results['artists']['items'][0]
        getFollowers(artist)
    else:
        return None

#Setup tkinter window
window = tkinter.Tk()
window.title("Live Spotify Follow Count")
window.geometry("500x500")

#Set up tkinter widgits
inp_artist_label = tkinter.Label(window, text="Artist")
inp_artist_ent = tkinter.Entry(window)
inp_artist_butt = tkinter.Button(window, text="Go", width=7, command=getArtist)

artist_name_label = tkinter.Label(window, text=" ", font=("Helvetica", 20))
followers_label = tkinter.Label(window, text="0", font=("Helvetica",35))

#Pack tkinter widgits
inp_artist_label.place(relx=0.5,y=30, anchor=CENTER)
inp_artist_ent.place(relx=0.5,y=50, anchor=CENTER)
inp_artist_butt.place(relx=0.5,y=75, anchor=CENTER)

artist_name_label.place(relx=0.5, rely=0.4, anchor=CENTER)
followers_label.place(relx=0.5, rely=0.5, anchor=CENTER)

#Show window
window.mainloop()
