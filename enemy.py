class Enemy:
    import random
    def encounter(random):
     while hp != 0:
        print('You have encountered a goblin!')
        enemy = 7
        move = input("What will you do (attack, heal, run):")
        if move == "attack":
            randomnumber = random.randint(1,3)
            attacknumber = input("pick a number 1-3 :")
            if attacknumber == randomnumber:
                enemy - 15
            else:
                print("You missed!")
        if move == "run":
            break
        if move == "heal":
           print(inventory)
           if potioncount != 0 or bigpotioncount != 0:
              askheal = input("which potion do you want to use(big potion or potion):")
              if askheal == "potion":
                 hp + 25
                 potioncount - 1
              if askheal == "bigpotion":
                 hp + 100
                 bigpotioncount - 1
           else:
              print("You do not have any potions!")
              
import random             
Enemy.encounter(random)

        


    