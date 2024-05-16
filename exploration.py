from combathandler import main
from village import village

class explore:
    def explorationloop(func):
        explorationquestion = input("Are you sure you wish to explore? (Y/N) :")
        if explorationquestion == "Y":
            main()
        elif explorationquestion == "N":
            func()

