import tkinter
from tkinter import BOTH, END, LEFT
import ftplib
ftp = ftplib.FTP()


def connectServer():
    ip = ent_ip.get()
    port = int(ent_port.get())
    
    try:
        msg = ftp.connect(ip,port)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to connect")

def loginServer():
    user = ent_login.get()
    password = ent_pass.get()
    try:
        msg = ftp.login(user,password)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        displayDir()
        lbl_login.place_forget()
        ent_login.place_forget()
        lbl_pass.place_forget()
        ent_pass.place_forget()
        btn_login.place_forget()
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to login")

        
def displayDir():
    dirlist = []
    dirlist = ftp.nlst()
    for item in dirlist:
        libox_serverdir.insert(END, item)

window = tkinter.Tk()
window.title("FTP Client")
window.wm_iconbitmap("favicon.ico")
window.geometry("1280x1084")

#Connect
lbl_ip = tkinter.Label(window, text="IP Address")
ent_ip = tkinter.Entry(window)
lbl_port = tkinter.Label(window, text="Port")
ent_port = tkinter.Entry(window)
btn_connect = tkinter.Button(window, text="Connect", command=connectServer)

#Server response text box
text_servermsg = tkinter.Text(window)

#Login
lbl_login = tkinter.Label(window, text="Username")
ent_login = tkinter.Entry(window)
lbl_pass = tkinter.Label(window, text="Password")
ent_pass = tkinter.Entry(window)
btn_login = tkinter.Button(window, text="Login", command=loginServer)

#Directory listing
lbl_dir = tkinter.Label(window, text="Directory listing:")
libox_serverdir = tkinter.Listbox(window)

#Options


#Place widgits
lbl_ip.place(x=20,y=20)
ent_ip.place(x=20,y=40)
lbl_port.place(x=20,y=60)
ent_port.place(x=20,y=80)
btn_connect.place(x=52,y=110)
text_servermsg.place(x=20,y=150)
lbl_login.place(x=20,y=550)
ent_login.place(x=20,y=570)
lbl_pass.place(x=20,y=590)
ent_pass.place(x=20,y=610)
btn_login.place(x=52,y=640)

lbl_dir.place(x=700,y=143)
libox_serverdir.place(x=700,y=165)

#Create
window.mainloop()
