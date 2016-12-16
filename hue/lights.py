from phue import Bridge
import time as t

b = Bridge('192.168.0.56')
l = 4

try:
    b.connect()
    print("Connected to bridge.")
except:
    print("Could not connect to bridge.")

def lightOff():
    try:
        b.set_light(l,'on',False)
        print("Light turned off.")
    except:
        print("Could not turn off light.")

def lightOn():
    try:
        b.set_light(l,'on',True)
        b.set_light(l,'bri',255)
        print("Light turned on.")
    except:
        print("Could not turn on light")

def lightBrightness(value):
    try:
        b.set_light(l,'on',True)
        b.set_light(l,'bri',value)
        print("Light brightness changed to " + str(value))
    except:
        print("Could not set light brightness.")
