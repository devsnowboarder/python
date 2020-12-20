


def count(str1, str2):
    c, j = 0, 0
    print(str1)
    print(str2)

    set_string1 = set(str1)
    print(set_string1)

    # set of characters of string2
    set_string2 = set(str2)
    print(set_string2)

    matched_characters = set_string1 & set_string2
    print(matched_characters)
    print("No. of matching characters are : " + str(len(matched_characters)))




def main():
    str1 ='aabcddekll12@'  # first string
    str2 = 'bb2211@55k'  # second string
    count(str1, str2)  # calling count function


# Driver Code
if __name__ == "__main__":
    main()