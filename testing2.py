import json

f = open('mydata.json')
team = json.load(f)

print(team['player'])
print(team['player']['health'])
print(team['player']['dmg'])