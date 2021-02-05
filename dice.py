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
time.sleep(3)
die=str(random.randint(1,6))
file=die+".txt"
with open(f"{file}") as f:
    face=f.read()
print(face)