import os
import discord
import shutil
from colorama import Fore, init
center = shutil.get_terminal_size().columns

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

os.system('title [Nightmare-Remade Paid MassDM] By AlexB - Main Menu')


buh = '''
  ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
  ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
  ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
  ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
AlexB#7653
'''
for line in buh.splitlines():
    print(f'\033[35m {line}'.center(center).replace("█",f"\033[0m█\033[35m"))

border = "\033[0m─"*center
print(border.center(center))

token = input(f'{gray}[{dblue}?{gray}]{white} Token:{Fore.RESET} ')
txt = input(f'{gray}[{dblue}?{gray}]{white} Message:{Fore.RESET} ')
input(f'{gray}[{dblue}!{gray}]{white} Press ENTER To Start!')

client = discord.Client()


@client.event
async def on_connect():
    for user in client.user.friends:
        try:
            await user.send(txt)
            print(f"{gray}[{green}-{gray}]{white} Messaged:{Fore.RED} {user.name}")
        except:
            print(f"{gray}[{red}-{gray}]{white} Couldn't Message:{Fore.RED} {user.name}")
            input(f'{gray}[{dblue}!{gray}]{white} Press ENTER To Start!')

client.run(token, bot=False)


