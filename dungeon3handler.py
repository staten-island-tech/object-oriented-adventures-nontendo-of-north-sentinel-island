import json
import random
from playerclass import *


def load_enemies(filename):
    with open(filename, 'r') as file:
        enemies = json.load(file)
    return enemies

def spawn_enemy(enemies):
    return random.choice(enemies)

def finalfantasycomplete():
    print("YOU HAVE SLAYED ALL 3 BOSSES AND SAVED NORTH SENTINAL ISLAND!!")
    print("For this.. we have granted you the greatest power of all .... ZIJUN MA'S AWESOME SAUCE BLADE (it does 172² x 0.45 damage)")
    player.damage = 13312.8
    print("You bask in the glory of the blade, soaking in its power")
    print("You have recieved Zijun Ma's Awesome Sauce Blade!")

def main():
    enemies = load_enemies('dungeon3enemies.json')  

    for _ in range(10):
        if player.hp <= 0:
            print("You have died :( ")
            return

        enemy = spawn_enemy(enemies)
        enemy['current_hp'] = enemy['hp'] 
        print(f"A wild {enemy['name']} appears!")

        while enemy['current_hp'] > 0 and player.hp > 0:
            choice = input("Choose an action H for heal, C for combat, E for escape: ")
            if choice.upper() == 'H':
                potion_choice = input("Do you want to use a minor or major potion? M for Minor, B for Major: ")
                if potion_choice.upper() == "M" and player.minor_potions > 0:
                    player.heal(player.max_hp * 0.25)
                    player.minor_potions -= 1
                    print(f"You now have a total of {player.minor_potions} minor potions")
                elif potion_choice.upper() == "B" and player.major_potions > 0:
                    player.heal(player.max_hp)
                    player.major_potions -= 1
                    print(f"You now have a total of {player.major_potions} major potions")
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
                            print(f"Your total gold is now {player.gold}")
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
                        print("You have died :( ")
                        return
                else:
                    print(f"{enemy['name']} misses!")
                
            elif choice.upper() == 'E':
                if random.random() < 0.05:
                    print("You managed to escape!")
                    break
                else:
                    print("Failed to escape!")

    boss = {
        "name": "Spidorah",
        "hp": 125,
        "golddrop": 0,
        "dmgperhit": 23,
        "loot": [""]
    }
    boss['current_hp'] = boss['hp']
    print(f"A wild {boss['name']} appears!")

    while boss['current_hp'] > 0 and player.hp > 0:
        choice = input("Choose an action H for heal, C for combat, E for escape: ")
        if choice.upper() == 'H':
            potion_choice = input("Do you want to use a minor or major potion? M for Minor, B for Major: ")
            if potion_choice.upper() == "M" and player.minor_potions > 0:
                player.heal(player.max_hp * 0.25)
                player.minor_potions -= 1
                print(f"You now have a total of {player.minor_potions} minor potions")
            elif potion_choice.upper() == "B" and player.major_potions > 0:
                player.heal(player.max_hp)
                player.major_potions -= 1
                print(f"You now have a total of {player.major_potions} major potions")
            else: 
                print("You have no potions left!")
        
        elif choice.upper() == 'C':
            if random.random() <= 0.8:
                print(f"{player.name} attacks {boss['name']}")
                boss['current_hp'] -= player.damage
                print(f"{boss['name']} takes {player.damage} damage!")
                if boss['current_hp'] <= 0:
                    print(f"{boss['name']} defeated!")
                    while True:
                        finalfantasycomplete()
                        reward_choice = input("Choose your reward: H for Permanent HP Buff, D for Permanent DMG Buff, G for Gold Drop: ")
                        if reward_choice.upper() == 'H':
                            player.upgrade_max_hp(50)
                            break
                        elif reward_choice.upper() == 'D':
                            player.upgrade_damage(10)
                            break
                        elif reward_choice.upper() == 'G':
                            player.gold += 50
                            print(f"You received 50 gold! Total gold: {player.gold}")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                    return
            else:
                print(f"{player.name} misses!")
            
            if random.random() <= 0.8:
                print(f"{boss['name']} attacks {player.name}!")
                player.take_damage(boss['dmgperhit'])
                if player.hp <= 0:
                    player.max_hp = 100
                    player.hp = 100
                    player.gold -= 50
                    player.minor_potions -=1
                    player.major_potions -=1
                    print("You have been died :( ")
                    print("You must really suck huh ... For that im gonna give you some nerfs >:)")
                    print(" ")
                    print("Max HP is now back to 100")
                    print(" ")
                    print("Player gold is reduced by 50")
                    print(" ")
                    print("Major and Minor Potions are reduced by 1 each")
                    print(" ")
                    print("Dignity decreased by 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
                    return
            else:
                print(f"{boss['name']} misses!")
            
        elif choice.upper() == 'E':
            if random.random() < 0.05:
                print("You managed to escape!")
                return
            else:
                print("Failed to escape!")

main()
