class dungeons:
    def dungeonsloop(func):
        from combathandler import main
        dungeoning = input("Are you sure you want to enter the dungeon? (Y/N): ")
        if dungeoning == "Y":
            print("You have entered a damp, dark dungoen...")
            main()
        elif dungeoning == "N":
            print("You have returned back to the village...")
            func()
dungeons()