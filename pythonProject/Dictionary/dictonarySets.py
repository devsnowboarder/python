
#tuples
Cities = ('Austin', 'Portland', 'Dallas')
print (Cities[0])

print (Cities)

citi_info = {'Austin': 81111,'Dallas': 91345}
print (citi_info['Dallas'])
print (citi_info)


#sets
city_names_set = {'Austin', 'Portland', 'Dallas','Austin'}
print (city_names_set)
for set_value in city_names_set:
	print (set_value)

#a set will not print any duplicate even assigned in a set
for set_value in city_names_set:
    print(set_value)

cityName = 'SanFrancisco'
dupSet=set()

for x in cityName:
     if ( x  in dupSet):
         print(" Duplicate "+x)
     dupSet.add(x)


## finding duplicate values in a list
lst2 = [3, 1, 5, 2, 1, 10, 3, 5, 10, 11, 12]

dupl = set() # create empty set

# loop trough the elements inside the list
for i in lst2:
    if lst2.count(i) > 1:
        dupl.add(i)

# show final data
print(lst2)
print(dupl)

