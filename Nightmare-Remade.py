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
    unlock()


def unlock():
    gui()
    menu()

def exit():
    os._exit(0)
def wb():
    os.system("cls")
    import utils.wbspammer
def spidermanbuilder():
    os.system("cls")
    import utils.spidermanbuilder


def gui():
    os.system('cls & title Nightmare-Remade : Made By AlexB#7653')
    print(f"""
                         {C}███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
                         {C}████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
                         {C}██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
                         {C}██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
                            {C}██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
{R}> Creator AlexB#7653     {C}╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

                                       {p1}──────────────────────────────────────────{w1}
                                        {p1}────────────────────────────────────────{w1}
                                         {p1}╔══════════════════╦═════════════════╗{w1}
                                         {p1}║    
                                         {p1}║           {w1}[{p1}1{w1}] WBSpammer    
                                         {p1}║        {w1}[{p1}2{w1}] SpidermanBuilder
                                         {p1}╚══════════════════╩═════════════════╝{w1} 
""")

def menu():
    x = input(f"""
{C}╔═[{pcname}@Nightmare]
{C}╚══[{p1}OPTION{C}]═>{RE} """)
    
    if x == '1':
        wb()

    elif x == '2':
          spidermanbuilder()
    

    else:
        unlock()

if __name__ == "__main__":  
    os.system("title Loading Nightmare-Remade...")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    for item in progressbar:
        time.sleep(0.1)
    progressbar.set_description(' Loading Nightmare-Remade: ')

time.sleep(3)
print("\n")

progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33])
for item in progressbar:
        time.sleep(0.1)
progressbar.set_description(' Loading utils: ')
start()