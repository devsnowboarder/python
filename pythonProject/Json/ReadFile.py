
import jsongit b

file = open('infodata.txt', 'r')
#print (file.read())
result = json.dumps(file.read())
print(result)

if 'Analyst' in result:
    print('Found')