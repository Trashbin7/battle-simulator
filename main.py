import time
import random
import os
from halo import Halo

spinner = Halo(text='Loading...', spinner='')

loop = 1
choice = 0
userhp = 0
enemyhp = 0


while loop == 1:
    print("-------------------------", end="")
    time.sleep(0.1)s
    print("-------------------------")
    time.sleep(0.1)
    print("Welcome", end="")
    time.sleep(0.1)
    print(" back", end="")
    time.sleep(0.1)
    print(" to", end="")
    time.sleep(0.1)
    print(" Battle", end="")
    time.sleep(0.1)
    print(" Simulator", end="")
    time.sleep(0.1)
    print("!\n\n")
    time.sleep(0.1)

    print("Choose Your Difficulty:\n")
    time.sleep(0.3)
    print("[1] - Baby Mode\n[2] - Easy Mode\n[3] - Normal Mode\n[4] - Hard Mode\n[5] - Chad Mode\n\n[404] - Not Found\n\n")
    choice = input("Pick one: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    spinner.start()
    time.sleep(2)
    
    choice = str(choice)

    if choice == "1":
        userhp = 10000
        enemyhp = 1
    elif choice == "2":
        userhp = 100
        enemyhp = 50
    elif choice == "3":
        userhp = 100
        enemyhp = 50
    elif choice == "4":
        userhp = 100
        enemyhp = 50
    elif choice == "5":
        userhp = 10
        enemyhp = 10000
    elif choice == "404":
        spinner.warn("Game could not be found.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

