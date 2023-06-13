#######################################################################################

import os
import shutil
import time 
import discord
import turtle
from tqdm import tqdm
from colorama import Fore, init

center = shutil.get_terminal_size().columns
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
    menu()

def exit():
    os._exit(0)


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

def gui():
    os.system('cls & title Nightmare-Remade Paid : Made By AlexB#7653')
    print(f"""
  _   _   _   _   _   _   _   _   _     _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
( N | i | g | h | t | m | a | r | e )-( - | R | e | m | a | d | e )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/\_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  Creator: AlexB#7653

╔═══════════════════════════════════════════╗
║       Nightmare-Remade Tool Selection       ║
╠═══════════════════════════════════════════╣
║ 1. TokenCrasher       ║ 2. Spider-Man        ║ 3. WBSpammer           ║
╠═══════════════════════════════════════════╣
║ 4. MassReport         ║ 5. MassDM             ║ 6. soon™               ║
╚═══════════════════════════════════════════╝
""")

def menu():
    x = input(f"""
{C}╔═[{pcname}@Nightmare-Remade Paid]
{C}╚══[{p1}OPTION{C}]═>{RE} """)
    
    if x == '1':
        tokencrasher()
    elif x == '2':
          spidermanbuilder()
    elif x == '3':
          wb()
    elif x == '4':
          reporter()
    elif x == '5':
          massDM()
    elif x == '6':
        print(f"{R}Not Released Yet{RE}")
        time.sleep(2)
        unlock()
    else:
        unlock()

if __name__ == "__main__":  
    os.system("title Loading Nightmare-Remade Paid...")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    for item in progressbar:
        time.sleep(0.1)
    progressbar.set_description(' Loading Nightmare-Remade Paid: ')

time.sleep(3)
print("\n")

progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33])
for item in progressbar:
        time.sleep(0.1)
progressbar.set_description(' Loading utils: ')
start()
