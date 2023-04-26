limit = 10000

enteredAmount = int(input("Please enter the amount you want to withdraw"))

if(enteredAmount <= limit):
    print("Continue with next steps")
else:
    print("Please enter the amount which less than or equal to limit")
