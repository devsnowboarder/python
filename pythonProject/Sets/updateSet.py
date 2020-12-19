from Sets.setClass import Set


class setTest(list):
        def printNameClass(self):
            for x in self:
                print('My Set' , x)

        def intersect(self, other):
            res = []
            for x in self:
                if x in other:
                    res.append(x)
            return Set(res)





s = set('ABC')
s2= set('DEF')
setX = setTest(s)
setY = setTest(s2)
print("Intersection " ,s,s2)




print (s)
#s.update('BCD')
##print (s)
#s.remove('DEF')
#print (s)
#s -= set('EFG')
#print (s)