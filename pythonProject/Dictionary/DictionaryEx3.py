released = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
        "iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012,
        "iphone 5" : 2012,
	}
print (released)

print('xxxx')

for x ,y in released.items():
    print(x)



for item in released:
    if "iphone 5" in released:
        print ("Key found")
        break
    else:
        print ("No keys found")

print (released.get("iphone 3G", "none"))


print ("-" * 10)
print ("iphone releases so far: ")
print ("-" * 10)
for release in released:
    print (release)

print()
print()





phones = released.keys()
print(phones)

print("-----------------")
phones = released.values()
print(phones)


print("-----------------")
for key, value in sorted(released.items()):
    print (key, value)

print()
for phones in sorted(released, key=len):
        print (phones, released[phones])

print()
count = {}
for element in released:
    count[element] = count.get(element, 0) + 1
print (count )

print('------------------')

for key, value in released.items():
    if  str(value) =='2012':
        print(" value ",value)
    else:
        print(value)


phoneList = list()
print('------------------')
for key, value in released.items():
    print(value)

print(phoneList)



for key, value in released.items():
    if  str(value) in  phoneList :
          phoneList.add(value)
    else:
        print(" duplicated  ",value)

for key , value in  released.items():
    print(key)

