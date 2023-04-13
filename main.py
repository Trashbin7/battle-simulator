# made by github.com/TrashBin7
# if there is a problem, dm me at "mertcinarsah#5188" in discord
# read readme.md for more info
import time
import random
import os


loop = 1
choice = 0
userhp = 0
enemyhp = 0
gameloop = 1
username = ""

def slowprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.03)

def fastprint(string):
    for letter in string:
        print(letter, end='', flush=True)



while loop == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    if username == "":
        slowprint("Welcome back to Battle Simulator!\n\n\n")
    else: 
        slowprint(f"Welcome back to Battle Simulator, {username}!\n\n\n")

    fastprint("Choose Your Difficulty:\n[1] - Baby Mode\n[2] - Easy Mode\n[3] - Normal Mode\n[4] - Hard Mode\n[5] - Chad Mode\n\n\n")
    
    choice = input("Pick one: ")
    
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
    if username == "":
        username = input("Username: ")
    else:
        namechange = input(f"Username (leave blank to continue with {username}): ")
        if namechange == "":
            print(f"welcome back, {username}")
        else:
            username = namechange
            print(f"username set as {username}")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Setting up the game...")
    time.sleep(1)
    gameloop = 1
    while gameloop == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"It's your turn.\n{username}: {userhp} hp | enemy: {enemyhp} hp\n\n[1] Attack - [2] Defend - [3] Heal\n\n")
        useranswer = input()
        defend = False
        if useranswer == "1":
            critical = random.randint(1, 10)
            time.sleep(0.5)
            if critical >= 8:
                print("Critical hit? ", end="")
                time.sleep(0.5)
                slowprint("YES!")
                dmg = random.randint(10, 12)
            else:
                print("Critical hit? ", end="")
                time.sleep(0.5)
                slowprint("no.")
                dmg = random.randint(2, 10)
            print()
            time.sleep(0.5)
            slowprint(f"You dealt {dmg} damage to the enemy.")
            enemyhp = enemyhp - dmg
            dmg = 0
            time.sleep(1)
        if useranswer == "2":
            print("You will block all enemy damages.")
            defend = True
            time.sleep(1)

        if useranswer == "3":
            healamount = random.randint(1, 10)
            print(f"you healed {healamount}")
            userhp = userhp + healamount
            time.sleep(1)


        print(f"\nEnemy turn\n\n")
        enemymove = random.randint(1, 2)
        if enemymove == 1:
            critical = random.randint(1, 10)
            time.sleep(0.5)
            if critical >= 8:
                print("Critical hit? ", end="")
                time.sleep(0.5)
                slowprint("YES!")
                dmg = random.randint(10, 12)
            else:
                print("Critical hit? ", end="")
                time.sleep(0.5)
                slowprint("no.")
                dmg = random.randint(2, 10)
            print()
            time.sleep(0.5)
            if defend == True:
                print("enemy attacked to you, but you had shield!")
            else:
                print(f"enemy dealt {dmg} to you!")
                userhp = userhp - dmg
            time.sleep(1)
        if enemymove == 2:
            healamount = random.randint(1, 10)
            print(f"enemy healed {healamount}")
            enemyhp = enemyhp + healamount
            time.sleep(1)
        time.sleep(1)
        if userhp <= 0 or enemyhp <= 0:
            gameloop = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{username}: {userhp} hp | enemy: {enemyhp} hp\n")
    if enemyhp <= userhp:
        print("you Won!")
    else:
        print("You Lost!")
    print("Press [ENTER] to play again.\n\n\nmade by github.com/TrashBin7")
    input()