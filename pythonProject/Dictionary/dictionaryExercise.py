# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

# get vs [] for retrieving elements
my_dict = {'name': 'Jack',
           'age': 26,
           'name2':'John',
           'age2':30,
           'name3': 'Angel',
           'age3':40
}

# Output: Jack
print(my_dict['name'])
print(my_dict['name2'])

# Output: 26
print(my_dict.get('age'))
print(my_dict.get('age2'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science','AAAA','Math','Math','Math','Math','Math','Math'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)


# Output: ['English', 'Math', 'Science']
print(list(marks.keys()))


print(my_dict)

for k,value in my_dict:
    print(k,"  ",value)