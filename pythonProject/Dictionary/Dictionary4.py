released = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
        "iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012,
        "iphone 5" : 2012,
	}

"""
for key, value in released.items():
    print(value,key)
"""


print()

for key, value in released.items():
    if 'iphone 4' in released.keys():
      print( key,value)
