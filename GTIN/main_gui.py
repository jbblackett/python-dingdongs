#GTIN-8 GUI TEST
#Import csv and tkinter modules
import tkinter
from tkinter import *
import csv

#Setup tkinter and wigits
w = tkinter.Tk()
w.geometry("600x600")
w.title("GTIN-8 Client")

#Initialise tkinter widgits
lbl_entry = tkinter.Label(w, text="Entry Box")
ent_entry = tkinter.Entry(w)
lbl_products_gtin = tkinter.Label(w, text="GTIN Code")
lbl_products_desc = tkinter.Label(w, text="Description")
lbl_products_price = tkinter.Label(w, text="Price")

lib_products_gtin = tkinter.Listbox(w, width=9)
lib_products_desc = tkinter.Listbox(w)
lib_products_price = tkinter.Listbox(w, width=7)

#Place tkinter widgets on window
lbl_entry.place(x=500,y=0)
ent_entry.place(x=500,y=10)

lbl_products_gtin.place(x=7,y=10)
lib_products_gtin.place(x=10,y=30)
lbl_products_desc.place(x=95,y=10)
lib_products_desc.place(x=70,y=30)
lbl_products_price.place(x=200,y=10)
lib_products_price.place(x=195,y=30)

#Main program
#Import products from file to list
with open("products.csv", 'rU') as f:
    reader = csv.reader(f)
    products = list(list(rec) for rec in csv.reader(f, delimiter=','))
for i in range(len(products)):
    lib_products_gtin.insert(END, products[i][0])
    lib_products_desc.insert(END, products[i][1])
    lib_products_price.insert(END, '£' + products[i][2])

w.mainloop()

