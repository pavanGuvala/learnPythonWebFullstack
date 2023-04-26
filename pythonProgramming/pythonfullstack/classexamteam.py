class Employ:
    companyName = "Google India Pvt Ltd"

    def __init__(self, name, employid, salary):
        self.name = name
        self.employid = employid
        self.salary = salary

    def getEmploySalary(self):
        return "EmploySalary : " + str(self.salary)

    def updateSalary(Self):
        Self.Salary = Self.Salary + 1.1
class TaTeam(Employ):
    def getMywork(self):
        print("we do not take care techincal hiring")
emp1 = Employ("pavan kumar", 9449,400000)
emp2 = Employ("anisha",9899,600000)

Ta1 = TaTeam("TaGuy",9435,900000)
Ta1.getMywork()
print(Ta1.getEmploySalary())
    
