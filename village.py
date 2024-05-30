from readmeimport import stuff

def explorationloop():
    from combathandler import main
    explorationquestion = input("Are you sure you wish to explore? (Y/N) :")
    if explorationquestion == "Y":
            print("You venture off into the unknown...")
            main()
    elif explorationquestion == "N":
            print("You return to the village")

class village:
    def enteringvillage():
      print("You are now entering the village...")
      while True: 
        villagequestion = input("What would you like to do? (Check manual, Shop, Explore, Dungeons): ")
        while villagequestion == "Shop":
            from shop import visit_shop
            visit_shop
            break
        if villagequestion == "Explore":
            explorationloop()
            village.enteringvillage()
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