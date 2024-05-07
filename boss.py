import time 
import sys



class Dungeon():


    def print_slow(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.04)
    print_slow("You are about to Enter the Slime Dungeon, Enter (Y/N) if you want to Enter or Return Back to the Village")
    chooseslime = (input(" (Y/N): "))
    if chooseslime.upper() == "Y":
        print_slow("You have Entered the Dungeon")
        print("")
        print_slow("You Have Encountered A Horde Of Slimes") 

    elif chooseslime.upper() == "N":
        print("You have returned back to the village")
