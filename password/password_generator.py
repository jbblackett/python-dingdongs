import random as r
import tkinter
from tkinter import *
from tkinter import ttk

#Initiate character lists
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
SYMBOLS = '!"£$%^&*()-_=+]}[{]}:;@#~/?.>,<'

#Function called by button to generate password0
def generatePassword():
    global var
    poschars = []
    password = ""
    length = var_length_wg.get()
    #Add characters to possible charaters based on checkboxes
    if bool_lower_wg.instate(['selected']):
        for i in range(len(LETTERS)):
            poschars.append(LETTERS[i])
    if bool_upper_wg.instate(['selected']):
        for i in range(len(LETTERS)):
            poschars.append(LETTERS[i].upper())
    if bool_nums_wg.instate(['selected']):
        for i in range(10):
            poschars.append(str(i))
    if bool_symbols_wg.instate(['selected']):
        for i in range(len(SYMBOLS)):
            poschars.append(SYMBOLS[i])
    #Loop as long as password length to create password
    for i in range(length):
        password += poschars[r.randint(0,len(poschars)-1)]
    #Change label text to password
    lbl_password_wg.config(text=password)

#Setup tkinter window
w = tkinter.Tk()
w.title("Password Generator")

#Setup tkinter widgits
var_length_wg = tkinter.Scale(w, from_=5, to=30, orient=HORIZONTAL)
bool_lower_wg = ttk.Checkbutton(w, text="Include lowercase letters")
bool_upper_wg = ttk.Checkbutton(w, text="Include uppercase letters")
bool_nums_wg = ttk.Checkbutton(w, text="Include numbers")
bool_symbols_wg = ttk.Checkbutton(w, text="Include symbols")
btn_generate_wg = tkinter.Button(w, text="Generate", command=generatePassword)
lbl_password_wg = tkinter.Label(w, text="")

#Place tkinter widgits
var_length_wg.pack()
bool_lower_wg.pack()
bool_upper_wg.pack()
bool_nums_wg.pack()
bool_symbols_wg.pack()
btn_generate_wg.pack()
lbl_password_wg.pack()

#Untick checkboxes
bool_lower_wg.state(['!alternate'])
bool_upper_wg.state(['!alternate'])
bool_nums_wg.state(['!alternate'])
bool_symbols_wg.state(['!alternate'])

bool_lower_wg.state(['!selected'])
bool_upper_wg.state(['!selected'])
bool_nums_wg.state(['!selected'])
bool_symbols_wg.state(['!selected'])

#Show tkinter window
w.mainloop()
