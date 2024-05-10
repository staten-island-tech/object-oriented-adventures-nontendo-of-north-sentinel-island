
import random 


class playercombat:

    

        hitpool = random.randint(1,2)
        while True: 
            initiater = input("Choose between (H/C/E) to initiate your actions: ")
            if initiater.upper() == "C":
                combatter = print("Choose Between 1-2, to hit your attack!")
            guesser = int(input("(1,2): "))
            
            if guesser == hitpool:
             print("You hit your attack!")
             print("uhhh we'll get this working once we finish the thing to update enemy data")
             break
            if guesser != hitpool:
             print("You didn't hit your attack :( ")
