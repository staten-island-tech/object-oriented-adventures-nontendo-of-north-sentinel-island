import time 
import sys




class Dungeon1():
    def print_slow(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.04)
    print_slow("You are about to Enter the Slime Dungeon, Enter (Y/N) if you want to Enter or Return Back to the Village")
    slimechooser = (input(" (Y/N): "))
    if slimechooser.upper() == "Y":
        print("")
        print_slow("You have Entered the Dungeon")
        print("")

    elif slimechooser.upper() == "N":
        print("")
        print_slow("You Have Returned to the Village")
        print(" ")

    
