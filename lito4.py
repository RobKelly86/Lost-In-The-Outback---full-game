from sys import exit
from sys import argv    #This is for the scoreboard.
script, filename = argv

# 'Lost In The Outback V1.1' Full Game.

# Below are a list of variables for the game
title = "Lost In The Outback"

# ------ End of the list of variables ------

#------- Functions ---------

print("\n")
print(f"-        ##################################          -")
print(f"-        ##                              ##          -")
print(f"-        ##    ", title ,"     ##          -")
print(f"-        ##                              ##          -")
print(f"-        ##################################          -")
print("\n")
print("\n")

def complete():
    print(f" Well done {username}, you made it out of the outback!")
    print("\n")
    print(" Please see the previous user who completed 'Lost In The Outback!''")
    print("\n")
    print(txt.read())
    print("\n")
    target = open(filename, 'w')
    line1 = username
    target.write(f"{line1}")
    print("\n")
    play = input()
    goodbye()

def dead():
    print("\n")
    print(f" You died, RIP {username}.")
    print(" Would you like to play again?")
    print("\n")
    choice = input("> ")

    if "yes" in choice:
        desert()
    elif "no" in choice:
        goodbye()
    else:
        goodbye()

def goodbye():
    print("\n")
    print("\n")
    print("Thank you for playing")
    print("\n")
    print("Created by Robert Kelly 2022.")
    print("\n")

def desert():
    print("\n")
    print(" You feel strong winds and sand pelting your face,")
    print(" you slowly open your eyes to the bright sun beaming down upon you.")
    print(" You're dazed with no idea how you got here")
    print(" In one direction you notice a body of water in the distance. In the other direction you notice a nearby building.")
    print(" What do you do?")
    print("\n")

    choice = input("> ")

    if "water" in choice or "body" in choice:
        lake()
    elif "building" in choice:
        building()
    else:
        desert()

def lake():
    print("\n")
    print(" What first seemed like a good choice, has turned into a nightmare.")
    print(" The water you seen was a mirarge. You are now even more tired than before.")
    print(" All is not lost, you still have options.")
    print(" Do you carry on walking until you find water or do you make your way to the building?")
    print("\n")

    choice = input("> ")

    if "walking" in choice or "carry on" in choice:
        riddle1()
    elif "building" in choice:
        building()
    else:
        lake()

def riddle1():
    print("\n")
    print(" As you walk through the desert you stumble upon a riddle.")
    print(" Answer the riddle correctly and you will escape the desert.")
    print(" Get the riddle wrong and you will die upon the sand.")
    print("\n")
    print(" How far can you run into a desert?")
    print("\n")

    choice = input("> ")

    if "half" in choice or "half-way" in choice:
        complete()
    elif "all the way" in choice:
        print("\n")
        print("Unfortunately the answer was 'Half way, the other half you are running out the desert'.")
        print("\n")
        print(" Ok, you didn't die, you have made your way to the nearby building")
        print("\n")
        play = input(" Hit enter to continue.")
        building()
    else:
        print("\n")
        print(" Unfortunately the answer was 'Half way, the other half you are running out the desert'.")
        print("\n")
        print(" Ok, you didn't die, you have made your way to the nearby building")
        print("\n")
        play = input(" Hit enter to continue.")
        building()


def building():
    print("\n")
    print(" Ahh, that's better. The sun finally off your back.")
    print(" You take stock of the room you enter.")
    print(" There is a safe to the front of the building and a door to the rear of the building.")
    print(" What would you like to do?")
    print("\n")


    choice = input("> ")

    if "safe" in choice:
        safe()
    elif "door" in choice or "rear" in choice:
        rear_building()
    else:
        building()



def safe():
    print("\n")
    print(" Please enter the 4 digit code to open the safe.")
    print("\n")
    print(" If you are unsure of the 4 digit code, you may need to go back and find some clues.")
    print("\n")


    choice = input("> ")

    if choice == "2652":
        car_unlocked = True
        safe_open()

    elif "back" in choice:
        building()

    else:
        print("\n")
        print(" Access denied, please use the correct code.")
        safe()

def rear_building():

    print("\n")
    print(" Out the back of the building you see a beatern up car with the number plate 'Enigma 26'. ")
    print(" You see a note on the wall, its a bit to far to read.")
    print(" What would you like to do?")
    print("\n")

    choice = input("> ")

    if "open" in choice or "car" in choice:
        print("\n")
        print(" Damm the car is locked, you'll need to find the keys.")
        print("\n")
        play = input("  Hit enter to go back.")
        print("\n")
        rear_building()

    elif "read" in choice or "note" in choice:
        note()

    elif "back" in choice or "building" in choice:
        building()

    elif "safe" in choice:
        safe()

    else:
        rear_building()


def note():
    print("\n")
    print(" This looks like a riddle..")
    print(" I used to be a '2', flip me and turn me around. Now put that infront of the original me.")
    print("\n")
    play = input("  Hit enter to go back.")
    print("\n")
    rear_building()

def safe_open():
        print("\n")
        print(" The safe is open, inside you find a set of car keys and can of coke.")
        print(" You now make your way back outside the back of the building.")
        print("\n")
        print(" The car starts first time!")
        print(" As you are about to drive away you have 1 final decision.")
        print(" left or right?")
        print("\n")

        choice = input("> ")

        if "left" in choice:
            print("\n")
            print(" Good choice, you find a smooth road to the nearest town.")
            print("\n")
            complete()

        elif "right" in choice:
            print("\n")
            print(" Rough roads, no sign of civilisation for hundreds of miles, but you make it.")
            print("\n")
            complete()

        else:
            safe_open()

def title():
    global username #This line allows the variable created in this function to be used outside the function.
    print(" Welcome, please enter your username.")
    print("\n")
    username = input("> ")
    print("\n")
    print(f" Thank you {username}.")
    print("\n")
    play = input(" Hit enter to begin you adventure..")
    desert()

txt = open(filename)

title()
