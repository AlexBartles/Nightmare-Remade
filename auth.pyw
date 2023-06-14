import os
import tkinter as tk
from tkinter import *

window = Tk()

def unlock():
    window.destroy()
    os.system("cls")
    os.system("python Nightmare-Remade-Paid.pyw")

def Licensecall():
    data = text.get("1.0", "end-1c").strip()
    if data == "AlexBartles" or data == "theav2" or data == "admin":
        text.replace(1.0, tk.END, "Correct!")
        unlock()
    else:
        text.replace(1.0, tk.END, "Incorrect!")

text=Text(window)
login=Button(window, command=Licensecall, text="Login")
text.insert(1.0, "")

text.pack()
login.pack()

window.mainloop()