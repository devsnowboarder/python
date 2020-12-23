


def anagram ( str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1==str2:
        return True
    else:
        return False



str1 ="keep"
str2 ="Peek"

if anagram(str1,str2):
     print("Yes")
else:
     print("no")
