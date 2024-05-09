
import time
import sys
import random 


class playercombat:
        def print_slow(str):
            for letter in str:
             sys.stdout.write(letter)
             sys.stdout.flush()
             time.sleep(0.001)
        print_slow("Would you like to Initiate Your Actions? ")
        initiater = input(" (H/C/E): ")
        hitpool = random.randint(1,3)

        if initiater.upper() == "C":
            combatter = print("Choose Between 1-3, to hit your attack!")
            guesser = int(input("(1,2,3): "))
        elif initiater.upper() != "C" or "H" or "E": 
            print("uh can you type correctly...")
        if guesser == hitpool:
            print_slow("You hit your attack!")
            print("placeholder")
        elif guesser != hitpool:
            print_slow("You didn't hit your attack :( ")
            