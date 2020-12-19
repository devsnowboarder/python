

def duplicateList(elements):

    returnList = list()
    print(elements)
    ElementsSet = set()
    for elm in Elements:
        ElementsSet.add(elm)

    for elm in ElementsSet:
        if Elements.count(elm) > 1:
            returnList.append(elm)

    return returnList




Elements =list()

Elements.append("JAVA");
Elements.append("J2EE");
Elements.append("JSP");
Elements.append("SERVLETS");
Elements.append("JAVA");
Elements.append("STRUTS");
Elements.append("JSP");


print(" duplicated items:  ",duplicateList(Elements))

singleList = list()

for item in Elements:
    if item not in singleList:
        singleList.append(item)
    else:
        print(item)


singleSet = set()

for item in Elements:
    if item not in singleSet:
        singleSet.add(item)
    else:
        print(item)
