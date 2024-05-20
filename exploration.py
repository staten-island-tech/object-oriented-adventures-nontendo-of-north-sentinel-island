

class explore:
    def explorationloop(func):
        from combathandler import main
        explorationquestion = input("Are you sure you wish to explore? (Y/N) :")
        if explorationquestion == "Y":
            print("You venture off into the unknown...")
            main()
        elif explorationquestion == "N":
            print("You return to the village")
            func()
explore()
