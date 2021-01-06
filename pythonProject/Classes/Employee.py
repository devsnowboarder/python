class Employee:

 raise_amount = 1.04

 def __init__(self,first,last,pay):
        self.first=first
        self.last = last
        self.pay = pay
        self.email = first +'.' +last + '@company.com'
 def fullname(self):
     return '{} {}'.format (self.first,self.last)

 def apply_rase(self):
     self.pay= int(self.pay *self.raise_amount)


emp_1= Employee('jime','wong',1000)
emp_2= Employee('Bob','lee',2000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

print(emp_1.pay)
emp_1.apply_rase()
print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.__dict__)
