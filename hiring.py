
gender=input("enter your gender")
age=int(input("enter your age"))
name=input("enter your name")
relationship=input("enter your relationship status")
if(gender=="male"):
    if(age>30):
        if(relationship=="unmarried"):
            print("you are selected")
    else:
        print("you are not selected")
if(gender=="female"):
    if(age>20):
        if(relationship=="unmarried"):
            print("you are eligible")
    else:
        print("you are not selected")
else:
    print("you are not selected")    