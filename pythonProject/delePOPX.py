# list of chars
ch_list = ['A', 'F', 'B', 'Z', 'O', 'L']

# Deleting the element with value 'B'
ch_list.remove('B')

# list: ['A', 'F', 'Z', 'O', 'L']
print(ch_list)

# Deleting 2nd element
ch_list.pop(1)

# list: ['A', 'Z', 'O', 'L']
print(ch_list)



# Deleting all the elements
ch_list.clear()

# list: []
print(ch_list)
