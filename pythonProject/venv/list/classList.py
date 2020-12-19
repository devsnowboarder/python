class mikeList:
    def __init__(self, xList, item):
        self.xlist = xList
        self.item = item

    def addList(self,item):
      # xlist.append(self.item)
       print('HELLO',xlist)

    def printList(self):
        return(self.xList)




li =['a','b','new','test','google','apple']
print(li)
test = mikeList(li,'oracle')

test.addList(li,'oracle')



