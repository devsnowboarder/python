class listfunction:
    def __init__(self, mikeList):
        self.list = mikeList

    def addList(self):
        return mikeList(self)




li =['a','b','new','test','google','apple']

myList(li,'Oracle')



li.append('Intel')

print( li )

li = li +[4,5]

print(li)

for x in li:
    print(x)
    if x =='Intel':
      print(" Intel is on the list")
    else:
       if  x != 'google':
         print ( "Google is missing ")
