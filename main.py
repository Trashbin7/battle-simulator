# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                 #
#                                                                 #
#                     Battle Simulator                            #
#                made by github.com/TrashBin7                     #
#                                                                 #
#                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
#
# this is one of the biggest projects i've made so far (i am a beginner).
# read readme.md for more info
# 19/4/2023 (DD/MM/YYYY)
#
#
# UNSTABLE


print("loading...")
import os
import random
import time
from replit import db

loop = 1
choice = 0
userhp = 0
enemyhp = 0
gameloop = 1
username = ""
remaining = 3
ultiname = ""
ultiid = 0
ultidesc = 0
playerturn = 0
pickedultimate = 0
ultianswer = 0
usertry = 0
admintry = 0


adminuser = os.environ['ADMIN_USERNAME']
adminpass = os.environ['ADMIN_PASSWORD']
# btw if you find the password dm me on discord
# mertcinarsah#5188


def slowprint(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.03)

def fastprint(string):
    for letter in string:
        print(letter, end='', flush=True)

def admin():
  userhp = input("Your health: ")
  enemyhp = input("Enemy health: ")
  username = usertry
  return userhp, enemyhp, username

def randomulti():
    ultiid = random.randint(1, 6)
    if ultiid == 1:
        ultiname = "Meteor Attack"
        ultidesc = "A powerful attack that rains down meteors from the sky, dealing massive damage to all enemies."
    elif ultiid == 2:
        ultiname = "Nova Blast"
        ultidesc = "A burst of energy that creates a massive explosion, dealing damage to all enemies in a wide area."
    elif ultiid == 3:
        ultiname = "Ultimate Healing"
        ultidesc = "A powerful healing ability that restores a large amount of health."
    elif ultiid == 4:
        ultiname = "Time Warp" 
        ultidesc = "Slows down your opponents' movements, giving you a chance to attack multiple times in a row."
    elif ultiid == 5:
        ultiname = "Mind Control"
        ultidesc = "Take over your opponent's mind, forcing them to attack their own teammates."
    elif ultiid == 6:
        ultiname = "Rick Astley's Shield"
        ultidesc = "Creates a powerful shield that absorbs all incoming damage."
    else:
        print("ERROR: no ultimate found")
    pickedultimate = 1


def ultimate():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"------------------------------\n\nName: {ultiname}\nDescription: {ultidesc}\nId: {ultiid}\n\nWARNING: you cannot play this round if you use your ultimate attack!\n\n[1] Use  -  [2] Cancel\n\n------------------------------\n\n")
    ultianswer = input("1-2: ")
    if ultianswer == "1":
        if ultiid == 1:
            dmg = random.randint(5, 10)
            print(f"You dealt {dmg} damage to the enemy.")
            enemyhp = enemyhp - dmg
            ultimatedmg = enemyhp
            return enemyhp
        if ultiid == 2:
            dmg = random.randint(5, 10)
            print(f"You dealt {dmg} damage to the enemy.")
            enemyhp = enemyhp - dmg
            ultimatedmg = enemyhp
            return enemyhp
        if ultiid == 3:
            healamount = random.randint(5, 10)
            print(f"{healamount}")
            userhp = userhp + healamount
            return userhp






while loop == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    if username == "":
        slowprint("Welcome back to Battle Simulator!\n\n\n")
    else: 
        slowprint(f"Welcome back to Battle Simulator, {username}!\n\n\n")

    fastprint("Choose Your Difficulty:\n[1] - Baby Mode\n[2] - Easy Mode\n[3] - Normal Mode\n[4] - Hard Mode\n[5] - Chad Mode\n\nWARNING: Unstable Version! get an older version or do not use the ultimate attack!\n")
    
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
    elif choice == "ADMIN":
      usertry = input("Username: ")
      if usertry == adminuser:
        admintry = input("Password: ")
        if admintry == adminpass:
          admin()
        else:
          print("Wrong username or password!")
      else:
        input("Password: ")
        print("Wrong username or password!")
    else:
        print("\n\n\nYou need to pick between 1-5!")
        time.sleep(0.5)
        print("Stop and Start to continue!")
        time.sleep(1.5)
        print("\n(you could continue if you want, but it would be REALLLY buggy and glichy. if you really want, press [ENTER].)")
        input()
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
    randomulti()
    time.sleep(0.5)

    gameloop = 1
    while gameloop == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"It's your turn.\n{username}: {userhp} hp | enemy: {enemyhp} hp\n\n[1] Attack - [2] Defend - [3] Heal")
        if remaining == 0:
            print(f"[4] Ultimate: {ultiname} (Ready)\n\n")
        else:
            print(f"[-] Ultimate: {ultiname} ({remaining} rounds left)\n\n")

        playerturn = 1
        while playerturn == 1:
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
                playerturn = 0
                time.sleep(1)
                if remaining > 0:
                    remaining = remaining - 1

            if useranswer == "2":
                print("You will block all enemy damages.")
                defend = True
                time.sleep(1)
                playerturn = 0
                if remaining > 0:
                    remaining = remaining - 1

            if useranswer == "3":
                healamount = random.randint(1, 10)
                print(f"you healed {healamount}")
                userhp = userhp + healamount
                time.sleep(1)
                playerturn = 0
                if remaining > 0:
                    remaining = remaining - 1
            
            if useranswer == "4":
                if remaining > 0:
                    print("Your ultimate attack isn't ready...")
                    time.sleep(0.5)
                    print("It's still your turn!")
                else:
                    ultimate()
            


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
            healamount = random.randint(1,10)
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