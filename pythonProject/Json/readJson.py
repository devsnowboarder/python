
import json

with open(r'jsondata.json') as f:
    data = json.load(f)
print(data)



if 'English' in data['Subjects'] :
    print('Englist')

print(data['name'])

if 'John' in data['name']:
    print(data['name'])
else:
    print("Not found")



result = json.dumps(data)
print(result)

print("\n", type(result))

if 'English' in result :
    print('Englist')


"""
file = open("infodata.json")
ny = json.load(file)
ny.keys()
"""

