# This is a test

Elements =list()

Elements.append("JAVA");
Elements.append("J2EE");
Elements.append("JSP");
Elements.append("SERVLETS");
Elements.append("JAVA");
Elements.append("STRUTS");
Elements.append("JSP");


print(Elements)
ElementsSet = set()
for elm in Elements:
    ElementsSet.add(elm)

for elm in ElementsSet:
    if Elements.count(elm) > 1:
        print(elm)


