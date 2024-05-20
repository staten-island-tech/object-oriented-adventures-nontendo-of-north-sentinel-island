# Game Title - Final Fantasy 178² x 0.45
# Player Character
Character has inventory with potions and buff coins
# Enemies
3 main types of enemies (all drop different buff coins)
## Example of Attack Code
```
def main():
    player = Player("Player")
    enemies = load_enemies('enemydata.json')

    while player.hp > 0:
        enemy = spawn_enemy(enemies)
        enemy['current_hp'] = enemy['hp'] 
        print(f"A wild {enemy['name']} appears!")

        while enemy['current_hp'] > 0 and player.hp > 0:
            choice = input("Choose an action H for heal, C for combat, E for escape: ")
            if choice.upper() == 'H':
                potion_choice = input("Do you want to use a minor or major potion? M for Minor, B for Major: ").upper()
                if potion_choice == "M" and player.minor_potions > 0:
                    player.heal(player.max_hp * 0.25)
                    player.minor_potions -= 1
                elif potion_choice == "B" and player.major_potions > 0:
                    player.heal(player.max_hp)
                    player.major_potions -= 1
                else: 
                    print("You have no potions left!")
            
            elif choice.upper() == 'C':
                if random.random() <= 0.8:
                    print(f"{player.name} attacks {enemy['name']}")
                    enemy['current_hp'] -= player.damage
                    print(f"{enemy['name']} takes {player.damage} damage!")
                    if enemy['current_hp'] <= 0:
                        print(f"{enemy['name']} defeated!")
                        if 'golddrop' in enemy and isinstance(enemy['golddrop'], list) and len(enemy['golddrop']) > 0:
                            gold_dropped = random.choice(enemy['golddrop'])
                            player.gold += gold_dropped
                            print(f"You found {gold_dropped} gold!")
                        if 'loot' in enemy and random.random() < 0.05:
                            loot = random.choice(enemy['loot'])
                            print(f"You found {loot}")
                        break
                else:
                    print(f"{player.name} misses!")
                
                if random.random() <= 0.8:
                    print(f"{enemy['name']} attacks {player.name}!")
                    player.take_damage(enemy['dmgperhit'])
                    if player.hp <= 0:
                        print("You have been diedd :( ")
                        break
                else:
                    print(f"{enemy['name']} misses!")
                
            elif choice.upper() == 'E':
                if random.random() < 0.05:
                    print("You managed to escape!")
                    break
                else:
                    print("Failed to escape!")
       
        if player.hp > 0:
            play_again = input("Do you want another instance of combat? (Y/N): ")
            if play_again.upper() != 'Y':
                print(f"{player.name} Has Stopped Fighting")
                break
        else:
            break
              
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
75 HP
Either 12 or 15 DMG per attack


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
- After certain achievements, The player will increase in max HP by increments of 25.
  
## Shop
Minor Potion -  Heals 25% of max hp, cost: 15 gold     
Major Potion -  Heals 100% of max hp, cost: 60 gold
Upgrades to attack: - 
25 gold - Tier 1 - +15% dmg
50 gold - Tier 2 - +15% dmg
75 gold - Tier 3 - +15% dmg
100 gold - Tier 4 - +15% dmg