# Write a program to check the given number is even and should be in the range of 1000 to 9999 and should be divisable by 4


def evennumber(n):
    if(n % 2 == 0):
        n=int(input("enter a even number "))
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
