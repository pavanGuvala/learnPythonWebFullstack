lower = int(input("enter the lower interval number:"))
upper = int(input("enter the upper interval number:"))
for num in range (lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%1)==0:
                break
            else:
                print(num)

