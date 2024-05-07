
  
class Enemy:
    def encounter(random):
     import random
     hp = 100
     print('You have encountered a goblin!')
     while hp != 0:
        enemy = 7
        if enemy <= 0:
           break
        move = input("what would you like to do now?: Attack, Heal, Run")
        if move == "Attack":
            randomnumber = random.randint(1,3)
            attacknumber = input("pick a number 1-3 :")
            if attacknumber == randomnumber:
                print("You missed!")
            else:
                print('You hit the enemy for 5 hp!')
                enemy - 5
        if move == "Run":
            break
        if move == "heal":
            import inventory
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
     print('You defeated the goblin')
import random             
Enemy.encounter(random)

        


    