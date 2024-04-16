# Game Title - Final Fantasy 178² x 0.45
# Player Character
Character has inventory with potions and buff coins
# Enemies
3 main types of enemies (all drop different buff coins)
## Example of Attack Code
```
class Enemy:
    import random
    def encounter(random):
     while hp != 0:
        print('You have encountered a goblin!')
        enemy = 100
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
```

## Slimes
Green Slimes - 10 hp   
drops 8 to 12 gold  
damage per hit: 10  

Blue Slimes - 17 hp    
drops 12 - 15        
damage per hit: 14
---- all slimes have 5% chance of slimy token which gives a 10% buff in attack


## Spider
all spiders come in swarms of 5
Spider - 5 hp, drops 3 gold  
damage per hit: 9

## Daddy long legs 
10 hp   
drops 5 gold  
damage per hit: 15

## Mommy longer legs 
25 hp     
drops 15 gold
damage per hit: 20

## Goblin
all goblins come in swarms of 5     
7 hp    
drops 7 -9 gold

## Spear goblins
6 hp    
drops 7 gold and 1 spears

### Spear (Item)
Obtained from killing spear goblins 
Cannot be reused
Damage: same damage as one sword attack except there is a 100% hit rate instead of a chance. 


# Dungeons
## Slime Dungeon 
fight 3 blue slimes, then the boss   
Boss: "Slime King - Amalgamaion of Slime"
hp: 75   
Damage per hit: 

## Goblin Dungeon
fight two swarms of goblins , or 5 each back to back, then boss
Boss name: “Gobzilla - Humanity’s Punishment”
100 HP
Either 15 or 20 DMG per attack

## Spider Dungeon

fight a swarm of spiders, then a daddy and mommy long legs
Boss Name: “Spidorah - The 24 legged Dragon”
125 HP
Either 20 or 25 DMG per attack


# Bosses
## "Slime King - Amalgamation of Slime"
![](https://static.wikia.nocookie.net/terraria_gamepedia/images/9/93/King_Slime.gif/revision/latest/scale-to-width-down/166?cb=20200523113558)
## "Gobzilla - Humanity's Punishment"
![](https://www.spriters-resource.com/resources/sheet_icons/51/54580.png?updated=1460951294)
## "Spidorah - 24 Legged Dragon"
![](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1d8e44cc-5e95-40bb-b98a-e5b53d55358d/d5buyir-ce2c320c-e487-4f42-b076-c4c9a0405613.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzFkOGU0NGNjLTVlOTUtNDBiYi1iOThhLWU1YjUzZDU1MzU4ZFwvZDVidXlpci1jZTJjMzIwYy1lNDg3LTRmNDItYjA3Ni1jNGM5YTA0MDU2MTMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.lIOXlcsPfBhui9jBrPRuCeHH-8lGIcnj-zrTAxAp560)


## Upgrades
- Values of upgrades (costs) increases in increments of 25
- NO ARMOR
- After certain achiecments, The player willincrease in max HP by increments of 25.
  
## Shop
Minor Potion -  Heals 25% of max hp, cost: 15 gold     
Major Potion -  Heals 100% of max hp, cost: 60 gold
Upgrades to attack: - 
25 gold - Tier 1 -
50 gold - Tier 2 -
75 gold - Tier 3 -
100 gold - Tier 4 -