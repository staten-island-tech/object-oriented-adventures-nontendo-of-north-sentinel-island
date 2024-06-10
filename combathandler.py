import json
import random
from playerclass import player



def load_enemies(filename):
    with open(filename, 'r') as file:
        enemies = json.load(file)
    return enemies

def spawn_enemy(enemies):
    return random.choice(enemies)



def main():
    enemies = load_enemies('enemydata.json')

    while player.hp > 0:
        enemy = spawn_enemy(enemies)
        enemy['current_hp'] = enemy['hp'] 
        print(f"A wild {enemy['name']} appears!")

        while enemy['current_hp'] > 0 and player.hp > 0:
            choice = input("Choose an action H for heal, C for combat, E for escape: ")
            if choice.upper() == 'H':
                potion_choice = input("Do you want to use a minor or major potion? M for Minor, B for Major: ")
                if potion_choice == "M" and player.minor_potions > 0:
                    player.heal(player.max_hp * 0.25)
                    player.minor_potions -= 1
                    print(f"You now have a total of {player.minor_potions} potions")
                elif potion_choice == "B" and player.major_potions > 0:
                    player.heal(player.max_hp)
                    player.major_potions -= 1
                    print(f"You now have a total of {player.major_potions}")
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
                            print("Your total gold is now")
                            print({player.gold})
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
            if play_again.upper() == 'N':
                print("You decide to lay down your sword and return to the village... COWARD!")
                break
        else:
            break
        
