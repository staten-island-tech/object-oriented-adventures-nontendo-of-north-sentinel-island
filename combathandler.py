import json
import random 
from shop import visit_shop

class player:
    def __init__(self, name, max_hp=100):
        self.name = name
        self.max_hp = max_hp
        self.damage = 10
        self.gold = 25
        self.minor_potions = 0
        self.major_potions = 0
    
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy['name']} for {self.damage} damage!")
        enemy['hp'] -= self.damage

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage.")
    
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
    
    def upgrade_damage(self, percentage):
        self.damage = int(self.damage * (1 + percentage / 100))
    
    def upgrade_max_hp(self, percentage):
        self.max_hp = int(self.max_hp * (1 + percentage / 100))
        self.hp = min(self.max_hp, self.hp)

def load_enemies(filename):
    with open(filename, 'r') as file:
        enemies = json.load(file)
    return enemies

def spawn_enemy(enemies):
    return random.choice(enemies)

def main():
    player = Player("Player")
    enemies = load_enemies('enemydata.json')

    while True:
        enemy = spawn_enemy(enemies)
        print(f"A wild {enemy['name']} appears!")

        while enemy['hp'] > 0 and player.hp > 0:
            choice = input("Choose an action H for heal, C for combat, E for escape: ")
            if choice.upper() == 'H':
                if player.minor_potions> 0:
                    player.heal(player.max_hp * 0.25)
                    player.minor_potions -= 1
                    print("You used a Minor Potion and healed yourself.")
                elif player.major_potions > 0:
                    player.heal(player.max_hp)
                    player.major_potions -= 1
                    print("You used a Major Potion and healed yourself fully.")
                else: 
                    print("You have no potions left!")
            
            elif choice.upper() == 'C':
                player.attack(enemy)
                if enemy['hp'] <= 0:
                    print(f"{enemy['name']} defeated!")
                    if 'golddrop' in enemy:
                        gold_dropped = random.choice(enemy['golddrop'])
                        player.gold += gold_dropped
                        print(f"You found {gold_dropped} gold!")
                    if 'loot' in enemy and random.random() < 0.05:
                        loot = random.choice(enemy['loot'])
                        print(f"You found {loot}!")
                    break
                # enemy
                if random.random() < 0.75:
                    print(f"{enemy['name']} attacks {player.name}!")
                    player.take_damage(enemy['dmgperhit'])
                    if player.hp <= 0:
                        print("You have been defeated!")
                        break
                else:
                    print(f"{enemy['name']} misses!")
            elif choice.upper() == 'E':
                if random.random() < 0.50:
                    print("You managed to escape!")
                    break
                
                else:
                    print("Failed to escape!")
            else: 
                print("Invalid choice. Try again.")

            if enemy['hp'] > 0 and player.hp > 0:
                continue_combat = input("Do you want to continue fighting? (Y/N): ")
                if continue_combat.lower() != "N":
                    break
        if player.hp <= 0:
            break

        visit_shop(player)

        play_again = input("Do you want another instance of fighting? (Y/N): ")
        if play_again.upper() != 'Y':
            break        
 
