from phue import Bridge
import time as t
import tkinter

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

def lightBrightness(value):
    #Set brightness to value (1-255)
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
on  = tkinter.Button(window, text="ON", command=lightOn)
off = tkinter.Button(window, text="OFF", command=lightOff)

#Place tkinter widgits
on.place(x=5,y=5,width=790,height=297.5)
off.place(x=5,y=300,width=790,height=297.5)

window.mainloop()
