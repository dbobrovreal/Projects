from tkinter import *
import tkinter as ttk
from get import calc

def button_numbers(frame1):
    button = ["7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            ".", "0","=", "/",
            "C"]
    r = 1
    c = 0
    for i in button:
        cmd = lambda x=i: calc(x)
        ttk.Button(frame1, text=i, command=cmd, width = 10).grid(row=r, column=c)
        c += 1
        if c > 3:
            c = 0
            r += 1