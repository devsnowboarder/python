# list containing data
lst1 =  [3, 1, 5, 1, 10, 3, 5, 10]
# create an empty set
duplicates = set()


# loop through elements and find matches
for i in lst1:
    if i not in duplicates:
        duplicates.add(i)


# show data
print(lst1)
print(duplicates)


## finding duplicate values in a list
lst2 = [3, 1, 5, 2, 1, 10, 3, 5, 10, 11, 12]




dupl = set() # create empty set



for i in lst2:
    if lst2.count(i) > 1:
        dupl.add(i)



print(lst2)
print(dupl)


