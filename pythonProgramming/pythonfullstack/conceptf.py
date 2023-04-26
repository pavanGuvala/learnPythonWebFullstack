citizen="indian"
familyincome = 800000
listofstudentcourses=["enginnering","mbbs","bds","becom","bsc"]


enteredCitizen = input('Please enter citizen : ')
enteredFamilyIcome = int(input('Please enter a your family income'))
enteredCourse = input("Please enter a course ")


isEligible = True

if(citizen == enteredCitizen):
    if(enteredFamilyIcome <= familyincome):
        if(enteredCourse in  listofstudentcourses):

            print("your eligible for schoar ship")
        else:
            isEligible = False
    else:
        isEligible = False
else:
    isEligible = False

if(isEligible == False):
    print("not eligible for scholarship")




    