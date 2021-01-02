import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

mylist=["name","age","city"]
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


for x in mylist:
    print(y[x])