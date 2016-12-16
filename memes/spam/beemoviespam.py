import time as t
import win32api,win32gui,win32con,win32com.client

def moveCursor(x,y):
    win32api.SetCursorPos((x,y))

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    t.sleep(0.1)

def typeString(string):
    for char in string:
        win32com.client.Dispatch("WScript.Shell").SendKeys(char)

def pressEnter():
    win32com.client.Dispatch("WScript.Shell").SendKeys("{ENTER}")
        
beemovie = open("Bee Movie.txt", "r")

t.sleep(5)
for line in beemovie:
    typeString(line)
    pressEnter()
    t.sleep(0.2)
