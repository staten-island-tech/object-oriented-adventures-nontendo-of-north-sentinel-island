#!/usr/bin/env python3

import json

# instantiate an empty dict
team = {}

# add a team member
playerjsondata = team['player'] = {'health': 100, 'dmg': 5}


with open('mydata.json', 'w') as f:
    json.dump(team, f)