

str ="1101111000000110"
count =0
one=0
max=0

for x in range(len(str)):
   # print(str[x])

    if str[x]== "1":
        count =count +1
        print(count)
    else:
         one=count
         if one > max:
             max=one
         count =0


print(" Max = ",max)

