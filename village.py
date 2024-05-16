import time
import sys
from exploration import explore

class village:
    def enteringvillage(): 
      print("You are now entering the village...")
      while True: 
        villagequestion = input("What would you like to do? (Shop, Explore, NPC Dialouge(WIP)): ")
        while villagequestion == "Shop":
            shopquestion = input("What would you like to buy? Here are your options (Upgrade Damage - 50)(Potion - 10)(Big Potion - 50): ")
            if shopquestion  == 'Upgrade Damage':
                print("change this once we get player json thingy working")
                greatquestion = input("Would you like to keep shopping?(Y/N): ")
                if greatquestion == "N":
                    break
            elif shopquestion == "Potion":
                print("playergold - 10 and potioncount +1 once we get inv and player json working")
                greatquestion = input("Would you like to keep shopping?(Y/N): ")
                if greatquestion == "N":
                    break
            elif shopquestion == 'Big Potion':
                print("playergold - 50 and bigpotioncount +1 once we get inv and player json working")
                greatquestion = input("Would you like to keep shopping?(Y/N): ")
                if greatquestion == "N":
                    break
        if villagequestion == "Explore":
            explore.explorationloop(village.enteringvillage)
        elif villagequestion == "NPC Dialouge":
            print("call in randomized npc dialouge class once finished")
        
village.enteringvillage()