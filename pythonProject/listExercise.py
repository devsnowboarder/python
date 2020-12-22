
mikeList =[]

mikeList.append(2)
mikeList.append(3)
mikeList.append(4)
mikeList.insert(2,5)

for x in mikeList:
    print(x)
    if x > 3  :
        print(" Max number" + str(x))


for x in range(len(mikeList)):
    print(x)