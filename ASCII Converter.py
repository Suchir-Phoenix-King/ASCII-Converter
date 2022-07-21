# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 18:25:54 2022

@author: PC_RC
"""

from tkinter import *

root = Tk()
root.title("ASCII Converter")

root.configure(background='lightblue')
root.geometry("400x400")

enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root, text = "Name in ASCII: ", bg = "lightpink", fg = "black")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        
btn = Button(root, text="Show name in ASCII", command=asciiConverter, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.5, anchor = CENTER)
label.place(relx=0.5, rely=0.6, anchor = CENTER)

root.mainloop()
