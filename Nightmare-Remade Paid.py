# Import modules
import os
import tkinter as tk
import turtle
import shutil
import time 
import discord
from colorama import Fore, init
from tkinter import ttk
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

def start():
    Licensecall()

def unlock():
    gui()

def exit():
    os._exit(0)

def wb():
    os.system("cls")
    os.system("cd utils")
    os.system("python wbspammer.py")

def spidermanbuilder():
    os.system("cls")
    os.system("cd utils")
    os.system("python spidermanbuilder.py")

def reporter():
    os.system("cls")
    os.system("cd utils")
    os.system("python reporter.py")

def tokencrasher():
    os.system("cls")
    os.system("cd utils")
    os.system("python tokencrasher.py")
    
def massDM():
    os.system("cls")
    os.system("cd utils")
    os.system("python massdm.py")

def soon():
    os.system("cls")
    print("Coming soon!")

def Licensecall():
    os.system("cls")
    os.system('cls & title Nightmare-Remade Paid : License Key')
    print(f"""
  _   _   _   _   _   _   _   _   _     _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
( N | i | g | h | t | m | a | r | e )-( - | R | e | m | a | d | e )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/\_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   
    """)
    license = input(f"""
{C}╔═[{pcname}@Nightmare-Remade Paid]
{C}╚══[{p1}LICENSE KEY OR WEBSITE USERNAME{C}]═>{RE} """)
    if license == "c4c2ob-v61lsq-mvq006-s1gmne-d6zm1m-onvv8b" or license == "9690zw-w6fnjm-bjubeb-o0rqpy-2mmlp4-wb4jt9" or license == "AlexBartles" or license == "theav2":
        print(f"{G}Correct!")
        time.sleep(1.5)
        unlock()
    else:
        print(f"{R}Incorrect!")
        time.sleep(1.5)
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
    root.title("Nightmare-Remade Paid V5 Refresh") # Create window title


    # TokenCrasher button
    tokencrasher_button = ttk.Button(root,text="TokenCrasher", compound=tk.LEFT, command=tokencrasher) #command property tells tkinter what you wanna execute when button is clicked
    tokencrasher_button.pack(ipadx=5,ipady=5,expand=True)


    # Spider-Man button
    spiderman_button = ttk.Button(root,text="Spider-Man",command=spidermanbuilder)
    spiderman_button.pack(ipadx=5,ipady=5,expand=True)

    # WBSpammer button
    wbspammer_button = ttk.Button(root,text="WBSpammer",command=wb)
    wbspammer_button.pack(ipadx=5,ipady=5,expand=True)

    # MassReport button
    massreport_button = ttk.Button(root,text="MassReport",command=reporter)
    massreport_button.pack(ipadx=5,ipady=5,expand=True)

    # MassDM button
    massdm_button = ttk.Button(root,text="MassDM",command=massDM)
    massdm_button.pack(ipadx=5,ipady=5,expand=True)

    # soon™ button
    soon_button = ttk.Button(root,text="soon™",command=soon)
    soon_button.pack(ipadx=5,ipady=5,expand=True)

    # Exit button
    exit_button = ttk.Button(root,text="Exit",command=lambda: root.destroy())
    exit_button.pack(ipadx=5,ipady=5,expand=True)

    # Keep GUI on display
    root.mainloop()

if __name__ == "__main__":
    start()
