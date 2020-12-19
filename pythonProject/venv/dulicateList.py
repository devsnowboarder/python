

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''
    setOfElems = set()

    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)
    return False


def reverseList(listOfElements):
    listOfElements.reverse()

    print(listOfElements)


def main():
    listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
    print(checkIfDuplicates_1(listOfElems))

    print(len(set(listOfElems)))
    print(checkIfDuplicates_2(listOfElems))

    mikeset = set()
    reverseList(listOfElems)
    for x in listOfElems:
        mikeset.add(x)

    print(mikeset)
    for n in mikeset:
        print(n)


if __name__ == '__main__': main()
