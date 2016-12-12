#Forever prints the cursor location
import win32api
import win32con
import time
import win32com.client

time.sleep(1)
win32api.SetCursorPos((141,1002))
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(3)
win32api.SetCursorPos((222,10))
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

win32com.client.Dispatch("WScript.Shell").SendKeys("B")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("r")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("a")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("d")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("l")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("e")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("y")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys(" ")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("i")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("s")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys(" ")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("g")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("a")
time.sleep(0.5)
win32com.client.Dispatch("WScript.Shell").SendKeys("y")
time.sleep(0.5)

win32com.client.Dispatch("WScript.Shell").SendKeys("{ENTER}")
