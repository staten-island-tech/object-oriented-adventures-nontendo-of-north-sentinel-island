import json
import random 

class Enemy: 
    def __init__(self, name, hp, damage, gold_drop, loot):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.gold_drop = gold_drop
        self.loot = loot
# placeholder :sob:
class Potion:
    def __init__(self, name, healing_percentage):
        self.name = name
        self.healing_percentage = healing_percentage

def load_enemies():
    with open("enemydata.json", 'r') as file:
        enemies_data = json.load(file)
    return [Enemy(enemy['name'], enemy['hp'], enemy['dmgperhit'], enemy['golddrop'], enemy['loot']) for enemy in enemies_data]
def load_potions():
    with open("potions.json", 'r') as file:
        potions_data = json.load(file)
    return [Potion(potion['name'], potion['healing_percentage']) for potion in potions_data]
def main(): 
    enemies = load_enemies()
    potions = load_potions()
    player_hp = 10
    player_max_hp = 10
    player_gold = 0 
    #inventory is placeholdin
    player_inventory = []
    player_damage = 1
    enemy_hp = 50
    while enemies:  

        current_enemy = random.choice(enemies)

        print(f"A {current_enemy.name} appears! ")

    while enemy_hp > 0 and player_hp > 0:

        correct_number = random.randint(1,3)
        
       

        action = input("Choose your action: Combat, Heal, Escape, (C/H/E): ").upper()

        if action == "C":
            initate = int(input("Choose a Number Between 1-3: "))

            if initate == correct_number: 
                print("You managed to hit the enemy! ")
                current_enemy.hp -= player_damage
                print(f"{current_enemy.name} HP: {current_enemy.hp}")
            else: 
                print("You missed :(. The enemy attacks!")

            # enemy attacks
            if random.random() < 0.75:
                print("The enemy hits you!")
                player_hp -= current_enemy.damage
                print(f"Player HP: {player_hp}")
            else:
                print("The enemey missed!")

        elif action == "H" and player_hp < 10: 
            print("Select a potion to use: ")
            for i, potion in enumerate(potions, start=1):
                print(f"{i}, {potion.name}")
            choice = int(input("Eneter the number of the potion: "))
            if 1 <= choice <= len(potions):
                chosen_potion = potions[choice - 1]
                if chosen_potion.name == "Minor Potion":
                    healing_amount = int(player_max_hp * chosen_potion.healing_percentage)
                elif chosen_potion.name == "Major Potion":
                    healing_amount = player_max_hp
                else:
                    print("Invalid potion choice. Try again.")
                    continue
                player_hp = min(player_max_hp, player_hp + healing_amount)
                print(f"You used {chosen_potion.name} and healed for {healing_amount} HP.")
                print(f"Player HP: {player_hp}/{player_max_hp}")
            else:
                print("Invalid potion choice.")
                continue

        elif action == "E": 
            if random.random() < 0.05:
                print("You succesfully escaped!") 
                break
            else:
                print("Escape attempt failed. Enemy attacks! ")
                player_hp -= current_enemy.damage
                print(f"Player HP: {player_hp}")

        else:
            print("Invalid actions. ")  
            continue
    
        if player_hp <= 0:
            print("You were defeated by the enemy.")
        break
    else: 
        print(f"You defeated the {current_enemy.name}!")
        enemies.remove(current_enemy)

        player_gold += random.choice(current_enemy.gold_drop) if isinstance(current_enemy.gold_drop, list) else current_enemy.gold_drop
        print(f"You gained {player_gold} gold")

        if random.random < 0.05:
            player_inventory.extend(current_enemy.loot)
            print(f"You obtanined: {', '.join(current_enemy.loot)}")
    
    if not enemies:
        print("Congratulations! You have defeated all enemies!")
        print(f"Final gold: {player_gold}")
        print("Final Inventory:", player_inventory)

if __name__ == "__main__":
    main() 