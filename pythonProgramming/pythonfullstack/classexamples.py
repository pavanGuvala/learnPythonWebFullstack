class Employ:
    companyName = "Google India Pvt Ltd"

    def __init__(self, name, employid, salary):
        self.name = name
        self.employid = employid
        self.salary = salary

    def getEmploySalary(self):
        return "EmploySalary : " + str(self.salary)

emp1 = Employ("pavan kumar", 9449, 400000)
emp2 = Employ("anisha ", 9899, 600000)
print(emp1.getEmploySalary(),emp2.getEmploySalary())
