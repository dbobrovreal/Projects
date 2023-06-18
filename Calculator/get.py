from tkinter import *
import math
import sys

def calc(key):
    if win.get() == "0":
        win.delete(0, END)
    win.insert(END, key)

    if key == "=":
        win.delete(win.index(END) - 1)
        result = eval(win.get())
        win.delete(0, END)
        print(result)
        win.insert(END, "=" + str(result))
        return
    elif key == "C":
        win.delete(0, END)
        win.insert(END, 0)


    if win.get()[0] == "=":
        str1 = "1234567890"
        if key in str1:
            win.delete(0, END) 
            win.insert(END, key)
            return
        else:
            win.delete(win.index(0))
            result = eval(win.get())
            win.delete(0, END)
            win.insert(END, str(result))

def field(frame):
    global win
    win =  Entry(frame, width=33)
    win.grid(row=0, column=0, columnspan=5)
    win.insert(END, 0)
