# Write a program to a check a special phone number or not 

# conditions number must be even and divisible by 4 and and must be digits

from commonlogic import evenCheck, diviSableBy4

def checkFor10Digits(n):
    if len(str(n)) == 10:
        return True
    else:
        return False
    

n = int(input("Please enter a phone number  "))

if(evenCheck(n) and diviSableBy4(n) and checkFor10Digits(n)):
    print("Yeaahh! its a special phone number")
else:
    print("Nop, its not a special number")