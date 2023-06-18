from tkinter import *
import tkinter as tk
from button import button_numbers
from get import field

window = tk.Tk()
window.title("Калькулятор")
window.geometry("650x400")

frame = Frame(window) 
frame.pack() 

field(frame)
button_numbers(frame)

window.mainloop()