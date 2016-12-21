from phue import Bridge
import time as t
import tkinter
from tkinter import HORIZONTAL

#Connect to bridge
b = Bridge('192.168.0.56')
l = 4

try:
    b.connect()
    print("Connected to bridge.")
except:
    print("Could not connect to bridge.")

def lightOff():
    #Turn off light
    try:
        b.set_light(l,'on',False)
        print("Light turned off.")
    except:
        print("Could not turn off light.")

def lightOn():
    #Turn on light
    try:
        b.set_light(l,'on',True)
        b.set_light(l,'bri',255)
        print("Light turned on.")
    except:
        print("Could not turn on light")

def lightBrightness():
    #Set brightness to value (1-255)
    value = brightness.get()
    try:
        b.set_light(l,'on',True)
        b.set_light(l,'bri',value)
        print("Light brightness changed to " + str(value))
    except:
        print("Could not set light brightness.")

#Setup tkinter window
window = tkinter.Tk()
window.title("Light Control")
window.geometry("800x600")
window.resizable(0,0)

#Create tkinter widgits
on              = tkinter.Button(window, text="ON", command=lightOn)
off             = tkinter.Button(window, text="OFF", command=lightOff)
brightness      = tkinter.Scale(window, from_ = 0, to = 255, orient = HORIZONTAL)
brightness_butt = tkinter.Button(window, text="SET BRIGHTNESS", command=lightBrightness)

#Place tkinter widgits
on.place(relx=0,y=5,width=395,height=297.5)
off.place(relx=0.5,y=5,width=395,height=297.5)
brightness.place(x=200,y=400, width=400)
brightness_butt.place(x=350,y=450)

window.mainloop()
