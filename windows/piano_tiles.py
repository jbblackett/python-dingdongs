import win32api,win32con,time,win32com.client,win32gui
from ctypes import windll

dc = windll.user32.GetDC(0)
tileColor = 2105376
tiles = [423,570,710,851]
y = 745

def getMousePos():
    return(win32gui.GetCursorPos())

def getPixelColor(x,y):
    return(windll.gdi32.GetPixel(dc,x,y))

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while True:
    for x in tiles:
        color = getPixelColor(x,y)
        if color == tileColor:
            click(x,y)
