class User:
    def __init__(self,name,phone,address,email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def getMyName(self):
        return self.name

    def getMyDetails(self):
        return "Name is : " + self.name + " ad from ",self.address
User1 = User("Pavan",7829393359,"anantapur","pavanguvvala25@gmail.com")
print(User1.getMyName())
print(User1.getMyDetails())