class employee():
    def __init__(self, name, age, id, salary):
      self.name = name
      self.age = age
      self.salary = salary
      self.id = id


class employee1():
    def __init__(self, name, age, salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class childemployee(employee1):
    def __init__(self, name, age, salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id


emp1 = employee1('harshit',22,1000,5555)

emp1 = employee1("harshit", 22, 1000, 1234)
emp2 = employee1("arjun", 23, 2000, 2234)
print(emp1.__dict__)
print(emp2.__dict__)

emp1 = employee1('harshit',22,1000,7777)
emp2 = childemployee('arjun',23,2000,7777)
print(emp1.age)
print(emp1.name)
