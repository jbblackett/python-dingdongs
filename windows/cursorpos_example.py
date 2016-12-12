#Moves the cursor to every pixel on the screen
import win32api

width = 1280
height = 1024
pixels = width * height

for i in range(width):
    for o in range(height):
        win32api.SetCursorPos((i,o))
        print("Done (" + str(i) + ", " + str(o) + ")") 

#My screen resolution
#1280 x 1024

#To move cursor
#win32api.SetCursorPos(x,y)
