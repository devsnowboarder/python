set1 = set()
print("Intial blank Set: ")
print(set1)

# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6, 7))
set1.add(9)
set1.add(9)




print(set1)


myList = list()
myList =[2,3,4,1,3,4,5,1,4]

set2 = set()

for x in myList:
    set2.add(x)

for elem in set2:
    if myList.count(elem) > 1:

        print(" duplicate " ,elem)




