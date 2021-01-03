sal_info=dict()
sal_info={'Austin':911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 89286,'Portland':101367}

#reassigns the salary for Atlanta
sal_info['Atlanta']= 92340
print (sal_info)

print(sal_info['Austin'])

for x in sal_info:
    print(x,"  ",sal_info[x])


if ('Seattle' not in sal_info):
	sal_info['Seattle']= 110340
else:
	print ("key exists")

print (sal_info)

del sal_info['Atlanta']
print (sal_info)