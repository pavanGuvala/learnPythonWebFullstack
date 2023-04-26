def scholarshipeligibility():
    citizen=input("enter name of the the citizen")
    familyincome=800000
    studentcourselist=["bcom","btech","mbbs","msc","degree"]
    if(citizen=="indian")and(familyincome<=800000):
        if("mbbs" in studentcourselist):
            print("you are eligible for scholardhip")

        else:
            print("you are not eligible for scholarship")
scholarshipeligibility()

