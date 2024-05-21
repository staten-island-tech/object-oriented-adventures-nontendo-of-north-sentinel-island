from readmeimport import stuff


class village:
    def enteringvillage(): 
      from exploration import explore
      print("You are now entering the village...")
      while True: 
        villagequestion = input("What would you like to do? (Check manual, Shop, Explore, Dungeons): ")
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
        elif villagequestion == "Dungeons":
            dungeonquestion123 = input('Which dungeon will you venture into, The Slime Dungeon, The Goblin Dungeon, or the Spider Dungeon? (1,2,3): ')
            if dungeonquestion123 == "1":
                areyousure = input("Are you sure you wish to take on the dungeon? It is highly reccomended to stock up on potions and upgrades beforehand (Y/N) :")
                if areyousure == "Y":
                    from dungeon1handler import main
                    main
                elif areyousure == "N":
                    break
            if dungeonquestion123 == "2":
                areyousure = input("Are you sure you wish to take on the dungeon? It is highly reccomended to stock up on potions and upgrades beforehand (Y/N) :")
                if areyousure == "Y":
                    from dungeon2handler import main
                    main
                elif areyousure == "N":
                    break
            if dungeonquestion123 == "3":
                areyousure = input("Are you sure you wish to take on the dungeon? It is highly reccomended to stock up on potions and upgrades beforehand (Y/N) :")
                if areyousure == "Y":
                    from dungeon3handler import main
                    main
                elif areyousure == "N":
                    break
                    
        elif villagequestion == "Check manual":
            print(stuff)