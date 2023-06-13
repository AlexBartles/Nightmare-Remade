# Import modules
import os
import tkinter as tk
import turtle
import shutil
import time 
import discord
from colorama import Fore, init
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

pcname = (os.getenv('COMPUTERNAME'))

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
dgreen = Fore.GREEN
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTMAGENTA_EX
dblue = Fore.MAGENTA
gray = Fore.LIGHTBLACK_EX
intents = discord.Intents.all()

p1 = '\033[35m' 
g1 = '\033[90m'
w1 = '\033[37m'
P = '\033[35m' # purple
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
RE = '\033[0m' # reset
Y = '\033[33m' # yellow
B = '\033[34m' # blue
LG = '\033[37m' # lightgrey

window=Tk()

def start():
    Licensecall()

def gui():
    # Display settings
    root = tk.Tk()  #Create application window

    # Display settings
    window_width = 600    #Set window height and width
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(0, 0)
    root.attributes('-topmost', 0)
    root.attributes('-alpha', 1)     #Adjust transparacy
    root.configure(background='#411593')
    root.title("Nightmare-Remade Paid V5 Refresh") # Create window title


    # TokenCrasher button
    tokencrasher_button = tk.Button(root,bg='#411593', fg='#ff3000',text="TokenCrasher", compound=tk.LEFT, command=tokencrasher) #command property tells tkinter what you wanna execute when button is clicked
    tokencrasher_button.pack(ipadx=5,ipady=5,expand=True)


    # Spider-Man button
    spiderman_button = tk.Button(root,bg='#411593', fg='#ff3000',text="Spider-Man", command=spidermanbuilder)
    spiderman_button.pack(ipadx=5,ipady=5,expand=True)

    # WBSpammer button
    wbspammer_button = tk.Button(root,bg='#411593', fg='#ff3000',text="WBSpammer", command=wb)
    wbspammer_button.pack(ipadx=5,ipady=5,expand=True)

    # MassReport button
    massreport_button = tk.Button(root,bg='#411593', fg='#ff3000',text="MassReport", command=reporter)
    massreport_button.pack(ipadx=5,ipady=5,expand=True)

    # MassDM button
    massdm_button = tk.Button(root,bg='#411593', fg='#ff3000',text="MassDM", command=massDM)
    massdm_button.pack(ipadx=5,ipady=5,expand=True)

    # soon™ button
    soon_button = tk.Button(root,bg='#411593', fg='#ff3000',text="soon™", command=soon)
    soon_button.pack(ipadx=5,ipady=5,expand=True)

    # Exit button
    exit_button = tk.Button(root,bg='#411593', fg='#ff3000',text="Exit", command=lambda: root.destroy())
    exit_button.pack(ipadx=5,ipady=5,expand=True)

    # Keep GUI on display
    root.mainloop()

def unlock():
    window.destroy()
    gui()

def exit():
    os._exit(0)

def wb():
    os.system("cls")
    import utils.wbspammer

def spidermanbuilder():
    os.system("cls")
    import utils.spidermanbuilder

def reporter():
    os.system("cls")
    import utils.reporter

def tokencrasher():
    os.system("cls")
    import utils.tokencrasher
    
def massDM():
    os.system("cls")
    import utils.massdm

def soon():
    os.system("cls")
    import utils.soon

def Licensecall():
    data = text.get("1.0", "end-1c").strip()
    if data == "c4c2ob-v61lsq-mvq006-s1gmne-d6zm1m-onvv8b" or data == "9690zw-w6fnjm-bjubeb-o0rqpy-2mmlp4-wb4jt9" or data == "AlexBartles" or data == "theav2" or data == "admin":
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


if __name__ == "__main__":
    start()
