import time
import sys
import random 


class playercombat:
        def print_slow(str):
            for letter in str:
             sys.stdout.write(letter)
             sys.stdout.flush()
             time.sleep(0.04)
        print_slow("Would you like to Initiate Your Actions? ")
        initiater = input(" (H/C/E): ")
        hitpool = random.randint(1,3)
        if initiater.upper() == "C":
            guesser = print("Choose Between 1-3, to hit your attack!")
            input("(1,2,3): ")
        if guesser == hitpool:
            print("Correct! ")