import time
import os
from tqdm import *

def endhandler():
    time.sleep(2)
    exit()

os.system("title Loading Nightmare-Remade...")
progressbar = tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
for item in progressbar:
    time.sleep(0.1)
progressbar.set_description(' Loading Nightmare-Remade: ')

print("Phased out!")
time.sleep(5)
endhandler()