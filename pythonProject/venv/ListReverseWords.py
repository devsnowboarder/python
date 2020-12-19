
listStr ="This is a test"

listWord = listStr.split()


finalStr =' '
for x in listWord:
    print(x[::-1])
    finalStr = finalStr+'  '+x[::-1]

print(finalStr)