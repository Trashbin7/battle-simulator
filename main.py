import time
import random
import os


loop = 1
choice = 0
userhp = 0
enemyhp = 0
gameloop = 1

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
    fastprint("Choose Your Difficulty:\n[1] - Baby Mode\n[2] - Easy Mode\n[3] - Normal Mode\n[4] - Hard Mode\n[5] - Chad Mode\n\n\n")
    
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
        enemyhp = 100
    elif choice == "4":
        userhp = 50
        enemyhp = 100
    elif choice == "5":
        userhp = 10
        enemyhp = 10000
    else:
        print("You need to pick between 1-5!")
        time.sleep(0.5)
        print("Picking 3 for you...")
        time.sleep(3)
        userhp = 100
        enemyhp = 100
    print("Setting up the game...")
    time.sleep(1)
    gameloop = 1
    while gameloop == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("It's your turn.\n\n[1] Attack - [2] Defend - [3] Heal")
        


        enemymove = random.randint(1, 3)        #todo