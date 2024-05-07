import json

f = open('mydata.json')
team = json.load(f)

print(team['player'])
print(team['player']['health'])
print(team['player']['dmg'])
print('You have''health left')



with open('mydata.json', 'w') as f:
    json.dump(team, f)

