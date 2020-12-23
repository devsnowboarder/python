

listA={1,4,5,6,7,3,2}
listB={3,4,5,9,0,11}
countList = list()
listSet = set()

for item in listB:
  countList.append(item)

print(countList)

for item in listA:
    countList.append(item)
    if countList.count(item) > 1:
        print(item)

listBlst = set()

for  x in listB:
    listBlst.add(x)

print(listBlst)

for x in listA:
    if x  in listB:
        print(x)