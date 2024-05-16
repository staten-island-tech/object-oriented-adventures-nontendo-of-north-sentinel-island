""" #!/usr/bin/env python3

import json

# instantiate an empty dict
team = {}

# add a team member
playerjsondata = team['player'] = {'health': 100, 'dmg': 5}


with open('mydata.json', 'w') as f:
    json.dump(team, f)



 """
import random 
def gold_drop(player, enemy):
                print(f"{player['name']} attacks {enemy['name']}")
                enemy['hp'] -= player.damage
                print(f"{enemy['name']} takes {player.damage} damage!")
                if enemy['hp'] <= 0:
                    print(f"{enemy['name']} defeated!")
                    if 'golddrop' in enemy:
                        gold_dropped = random.choice(enemy['golddrop'])
                        player.gold += gold_dropped
                        print(f"You found {gold_dropped} gold!")
                    if 'loot' in enemy and random.random() < 0.05:
                        loot = random.choice(enemy['loot'])
                        print(f"You found {loot}")
gold_drop({'name':'steve', 'damage':75},{
        "name": "Blue Slime",
        "hp": 17,
        "golddrop": [12,13,14,15],
        "dmgperhit": 14,
        "loot": ["Slimey Emblem"]
    },)