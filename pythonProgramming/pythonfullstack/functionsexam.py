def evennumber(n):
    if(n % 2 == 0):
        n=int(input("enter a even number"))
        True
    else:
        print("enter an even number")    

def checkrange(n):
    if(n >= 1000 and n <= 9999):
        return True
    else:
        return False

def  isdivisibleby4(n):
    if(n % 4 == 0):
        return True
    else:
        return False

n = int(input("please enter a number"))

if(evennumber(n) and checkrange(n) and isdivisibleby4(n)):
    print(n,"is a special number")
else:
    print(n," it is not a special number")

def phoneNumber(n):

    phoneNumber = input("please enter your phone number")
if  len(phoneNumber  == 10):
    formatedNumber  = int(phoneNumber)
    if(evencheck(formatedNumber) and divisible4(formatedNumber)):
        print("its a special phone number") 
    else:
        print("Not a special phone number")
else:
    print("please enter a valid phone number")            