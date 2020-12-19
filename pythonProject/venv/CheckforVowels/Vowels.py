# Python program to accept the strings
# which contains all the vowels

# Function for check if string
# is accepted or not
def check(string):
    string = string.lower()

    # set() function convert "aeiou"
    # string into set of characters
    # i.e.vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels = set("aeiou")

    # set() function convert empty
    # dictionary into empty set
    s = set({})

    # looping through each
    # character of the string
    for char in string:

        if char in vowels:
            s.add(char)
        else:
            pass

    if len(s) == len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")

    # Driver code


if __name__ == "__main__":
    string = "SEEquoiaL"

    # calling function
    check(string)