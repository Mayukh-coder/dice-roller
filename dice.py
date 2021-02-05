import keyboard
import os
import random
import time
os.system('cls')
print('''
This is a electronic dice. Press enter to the roll the dice.
                               ______
                   .-------.  /\     \ 
                  /   o   /| /o \  o  \ 
                 /_______/o|/   o\_____\ 
                 | o     | |\o   /o    /
                 |   o   |o/ \ o/  o  /
                 |     o |/   \/____o/
                 '-------'

''')
keyboard.wait('Enter')
os.system('cls')
def roll_dice():
    die=str(random.randint(1,6))
    file=die+".txt"
    with open(f"{file}") as f:
        face=f.read()
    print(face)
    print("Press enter to roll again.")
    keyboard.wait('Enter')
    os.system('cls')
    roll_dice()

roll_dice()