#name = input("student percentage:")
percentage=int(input("Please enter percentage:"))

#if ("student percentage>90 and student percentage >75 or studentpercentage>60 and studentpercentage>35 )
if(percentage >= 90):
    print("you got good percentage with a+ grade")
elif(percentage>=75):
    print("you got good percentage with a grade")
elif(percentage>=60):
    print("you got good percentage with b grade")
elif(percentage >= 35):
    print("you got average percentage with c grade")
else:
    print("Yor are not cleared the exam")




