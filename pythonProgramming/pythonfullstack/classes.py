class Employee:
   def __init__(self,name,age,salary,address):
    self.name = name
    self.age = age
    self.salary = salary
    self.address = address

employ1 = Employee("sunny",23,150000,"anantapur")
employ2 = Employee("bunny",26,180000,"banglore")

print(employ1.salary, employ1.address)



