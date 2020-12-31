
import json

with open(r'jsondata.json') as f:
    data = json.load(f)
print(data)

print(data['name'])

if 'John3' in data['name']:
    print(data['name'])

"""
file = open("infodata.json")
ny = json.load(file)
ny.keys()
"""

