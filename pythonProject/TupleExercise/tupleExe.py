tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 ,5,6,7);
tup4 = (1, 44, 34, 44, 5 ,6,7);
tup3 = "a", "b", "c", "d";

print ("tup1[0]: ", tup1[0])
print( "tup2[1:5]: ", tup2[1:5])

tup3 = tup1 + tup2;
print( tup3 )

for x in range(0, len(tup1)) :
    print(x)
    print(tup1[x])

print("=============")
for x in tup1:
    print(x)

dupItem = list()
print(tup4)

for x in tup4:
    dupItem.append(x)


for x in tup2:
    if x in tup4:
        print( "duplicate ",x)