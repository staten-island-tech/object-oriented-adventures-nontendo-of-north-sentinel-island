class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = 100
        self.damage = 5
        self.gold = 100
        self.minor_potions = 1
        self.major_potions = 1
    
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy['name']} for {self.damage} damage!")
        enemy['hp'] -= self.damage

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage. Remaining HP: {self.hp}/{self.max_hp}")
    
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} healed for {amount} HP. Current HP: {self.hp}/{self.max_hp}")
    
    def upgrade_damage(self, percentage):
        self.damage = int(self.damage * (1 + percentage / 100))
    
    def upgrade_max_hp(self, percentage):
        self.max_hp = int(self.max_hp * (1 + percentage / 100))
        self.hp = min(self.max_hp, self.hp)

player = Player("Player")