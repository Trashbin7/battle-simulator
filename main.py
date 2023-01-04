import time
import random
import os


loop = 1
choice = 0
userhp = 0
enemyhp = 0


def loading(value):
    if value == "start":
        time.sleep(0.5)
        for i in range(2):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[----] Loading...")
            time.sleep(0.025)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[=---] Loading...")
            time.sleep(0.025)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[==--] Loading...")
            time.sleep(0.025)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[===-] Loading...")
            time.sleep(0.025)            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[====] Loading...")
            time.sleep(0.025)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[-===] Loading...")
            time.sleep(0.025)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[--==] Loading...")
            time.sleep(0.025)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[---=] Loading...")
            time.sleep(0.025)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[----] Loading...")
            time.sleep(0.2)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[----] Loading done.")

def slowprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.03)

def fastprint(string):
    for letter in string:
        print(letter, end='', flush=True)



while loop == 1:
    print("--------------------------------------------------")
    slowprint("Welcome back to Battle Simulator!\n\n\n")
    fastprint("Choose Your Difficulty:\n[1] - Baby Mode\n[2] - Easy Mode\n[3] - Normal Mode\n[4] - Hard Mode\n[5] - Chad Mode\n\n[404] - Not Found\n\n\n")
    
    loading("start")
    
    choice = input("Pick one: ")
    os.system('cls' if os.name == 'nt' else 'clear')
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
        print("Game could not be found.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

