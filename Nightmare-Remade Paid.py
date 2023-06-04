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
    user()


def unlock():
    gui()
    menu()

def exit():
    os._exit(0)


def user():
    os.system("cls")
    os.system('cls & title Nightmare-Remade Paid : User')
    print(f"""
                         {C}███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
                         {C}████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
                         {C}██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
                         {C}██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
                         {C}██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
                         {C}╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    """)
    username = input(f"""
{C}╔═[{pcname}@Nightmare-Remade Paid]
{C}╚══[{p1}USERNAME{C}]═>{RE} """)
    if username == "theav2" or username == "alex" or username == "admin":
        print(f"{G}Correct!")
        time.sleep(1.5)
        pw()
    else:
        print(f"{R}Incorrect!")
        time.sleep(1.5)
        user()

def pw():
    os.system("cls")
    os.system('cls & title Nightmare-Remade : Password')
    print(f"""
                         {C}███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
                         {C}████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
                         {C}██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
                         {C}██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
                         {C}██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
                         {C}╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    """)
    password = input(f"""
{C}╔═[{pcname}@Nightmare-Remade Paid]
{C}╚══[{p1}PASSWORD{C}]═>{RE} """)
    if password == "Socksaregayasdx" or password == "201055" or password == "root":
        print(f"{G}Correct!")
        time.sleep(1.5)
        unlock()
    else:
        print(f"{R}Incorrect!")
        time.sleep(1.5)
        pw()

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
                         {C}███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
                         {C}████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
                         {C}██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
                         {C}██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
                            {C}██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
{R}> Creator AlexB#7653     {C}╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

                                       {p1}──────────────────────────────────────────{w1}
                                        {p1}────────────────────────────────────────{w1}
                                         {p1}╔══════════════════╦═════════════════╗{w1}
                                         {p1}║ {w1}[{p1}1{w1}] TokenCrash   {p1}║ {w1}[{p1}2{w1}] Spiderman   {p1}║{w1}
                                         {p1}║ {w1}[{p1}3{w1}] WBSpammer    {p1}║ {w1}[{p1}4{w1}] MassReport  {p1}║{w1}
                                         {p1}║ {w1}[{p1}5{w1}] MassDM       {p1}║ {w1}[{p1}6{w1}] soon        {p1}║{w1}
                                         {p1}╚══════════════════╩═════════════════╝{w1} 
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
