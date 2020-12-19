people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'JImmy', 'age': '22', 'sex': 'Female'},
          }

people[4] = {}

people[4]['name'] = 'Luna'
people[4]['age'] = '24'
people[4]['sex'] = 'Female'
people[4]['married'] = 'No'



for i in range(1,5):
    print(people[i]['name'])
    print(people[i]['age'])
    print(people[i]['sex'])

    print(' ')


for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])