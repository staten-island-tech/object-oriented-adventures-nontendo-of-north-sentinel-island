import time
import sys

class village:
    def enteringvillage():
        print("You are now entering the village...")
        villagequestion = input("What would you like to do? (Shop, Explore, NPC Dialouge(WIP))")
        if villagequestion == "Shop":
            shopquestion = input("What would you like to buy? Here are your options (Upgrade Damage - 50)(Potion - 10)(Big Potion - 50)")
            if shopquestion  == 'Upgrade Damage':
                print("change this once we get player json thingy working")
            elif shopquestion == "Potion":
                print("playergold - 10 and potioncount +1 once we get inv and player json working")
            elif shopquestion == 'Big Potion':
                print("playergold - 50 and bigpotioncount +1 once we get inv and player json working")
        elif villagequestion == "Explore":
            print("call in exploration class once finished")
        elif villagequestion == "NPC Dialouge":
            print("call in randomized npc dialouge class once finished")
        else:
            print("Please type again.")
        