hindimarks = int(input("hindi marks :\t"))
kannadamarks = int(input("kannada marks :\t"))
englishmarks = int(input("english marks :\t"))
mathsmarks = int(input("maths marks :\t"))
sciencemarks = int(input("science marks :\t"))
socialmarks = int(input("social marks :\t"))


# (480/600)*100 = 70

# Find a percentage of total marks

totalPercentage = ((hindimarks + englishmarks + mathsmarks + sciencemarks + socialmarks + kannadamarks)/600)*100
print("Percentage of total marks", totalPercentage)



if(totalPercentage <= 35):
    print("Soory, you failed in exams with grade F ")
elif(totalPercentage > 35 and totalPercentage <= 55):
    print(" just passed in exams grade is : D ")
elif(totalPercentage > 55 and totalPercentage <= 60):
    print("passed in exams grade is : C ")
elif(totalPercentage > 60 and totalPercentage <= 75):
    print("Average marks grade is : B ")
elif(totalPercentage > 75 and totalPercentage <= 90):
    print("got good marks grade is : A ")
elif(totalPercentage > 90 and totalPercentage <= 100):
    print("excellent marks and his grade is : A+ ")
else:
    print("enter the marks and range of 1 to 100")

