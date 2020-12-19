
def main():
    aList = range(0,199,2)

    secarhKey = int (raw_input("Enter integer search key: "))

    if secarhKey in aList:
      print( "Found at index :", aList.index ( secarhKey))
    else:
      print ("Value not found")

if __name__ == '__main__': main()