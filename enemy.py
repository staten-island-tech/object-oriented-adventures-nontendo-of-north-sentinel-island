
  
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

        

class enemydata():
    def green_slime(self):
        self.name = "Green Slime"
        self.hp = 10
        self.golddrop = 8
        self.dmgperhit = 10
        self.loot = "Slimey Emblem"
    def blue_slime(self):
        self.name = "Blue Slime"
        self.hp = 17
        self.golddrop = 12
        self.dmgperhit = 14
        self.loot = "Slimey Emblem"
    def spider(self):
        self.name = "Spider"
        self.hp = 5
        self.golddrop = 3
        self.dmgperhit = 9
        self.loot = "Legged Emblem"
    def daddy_long_legs(self):
        self.name = "Daddy Long Legs"
        self.hp = 10
        self.golddrop = 5
        self.dmgperhit = 15
        self.loot = "Legged Emblem"
    def mommy_longer_legs(self):
        self.name = "Mommy Longer Legs"
        self.hp = 25
        self.golddrop = 15
        self.dmgperhit = 20
        self.loot = "Legged Emblem"
    def goblin(self):
        self.name = "Goblin"
        self.hp = 7
        self.golddrop = 8
        self.dmgperhit = 6
        self.loot = "Goblin Emblem"
    def spear_goblin(self):
        self.name = "Spear Goblin"
        self.hp = 6
        self.golddrop = 7
        self.dmgperhit = 8
        self.loot = "Legged Emblem"
    def slime_king(self):
        self.name = "Slime King"
        self.hp = 75
        self.golddrop = 0
        self.dmgperhit = 14
        self.loot = ""
    def gobzilla(self):
        self.name = "Spider"
        self.hp = 100
        self.golddrop = 0
        self.dmgperhit = 17
        self.loot = ""
    def spidorah(self):
        self.name = "Spider"
        self.hp = 125
        self.golddrop = 0
        self.dmgperhit = 23
        self.loot = ""
   
    