class Employee:
   def __init__(self, id,name):
       self.id=id
       self.name=name

   def display(self):
       print("Hello my id is :", self.id)
       print("My name is :", self.name)

e1=Employee(1, 'Nithin')
e1.display()
e2=Employee(2, 'Arjun')
e2.display()